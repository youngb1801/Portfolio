#!/usr/local/bin/python3

# load required packages
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',100)
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')
import tensorflow as tf
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils import class_weight


# load data
train_df = pd.read_csv('/Users/bretyoung/Documents/GitHub/DSC_680_data/drugsCom_raw/drugsComTrain_raw.tsv', sep = '\t')
test_df = pd.read_csv('/Users/bretyoung/Documents/GitHub/DSC_680_data/drugsCom_raw/drugsComTest_raw.tsv', sep = '\t')

# remove na values from DataFrame
train_df = train_df.dropna()
test_df = test_df.dropna()

# exploration
def explore(df):
    print("Shape: ", df.shape, "/n")
    print(df.dtypes, "/n")
    print(df.head(), "/n")
    # numeric data statistics
    print(df.describe())
    df.hist(figsize=(14,14), xrot=45)
    plt.show()
    # categorical data statistics
    print(df.describe(include = 'object'))
    for column in df.select_dtypes(include = 'object'):
        if df[column].nunique() < 10:
            sns.countplot(y = column, data = df)
            plt.show()


explore(train_df)

# unbalanced classes
condition_counts = train_df['condition'].value_counts()
print(condition_counts)

# reduce the number of classes to anything with more than 1000 reviews
condition_counts_1000 = condition_counts[condition_counts > 1000]

print(len(condition_counts_1000))

counts_1000_list = list()
for idx, name in enumerate(condition_counts_1000.index.tolist()):
  counts_1000_list.append(name)

train_df = train_df[train_df['condition'].isin(counts_1000_list)]
test_df = test_df[test_df['condition'].isin(counts_1000_list)]

# visualiztions
fig, ax = plt.subplots(1, 1)
ax = sns.countplot(x = 'condition', data = train_df)
ax.set_title('Distribution of Conditions')
fig.show()

# set data and labels
x_train = train_df['review']
x_test = test_df['review']
y_train = train_df['condition']
y_test = test_df['condition']

# labels to one hot endoced
def prepare_targets(y_train, y_test):
    one_hot = LabelBinarizer()
    one_hot.fit(y_train)
    y_train = np.argmax(one_hot.transform(y_train), axis = 1)
    y_test_one_hot = one_hot.transform(y_test)
    y_test = np.argmax(one_hot.transform(y_test), axis = 1)
    y_test_rev = one_hot.inverse_transform(y_test_one_hot)
    return y_train, y_test, y_test_one_hot, y_test_rev

y_train, y_test, y_test_one_hot, y_test_rev = prepare_targets(y_train, y_test)

# create weights for classes
class_weights = class_weight.compute_class_weight('balanced', np.unique(y_train), y_train)

weights = dict(enumerate(class_weights))
print(weights)

# vectorize text
vocab_size = 1500
review_len_max = 200
encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens = vocab_size,
    output_sequence_length = review_len_max)

# develop vocabulary
encoder.adapt(x_train.values)

# vectorize text
x_train = encoder(x_train)
x_test = encoder(x_test)

# baseline model; all predictions birth control
count_bc = condition_counts['Birth Control']
base_acc = count_bc/len(y_train)
print(base_acc)

print('Training input shape: ', x_train.shape)
print(len(x_train))
print(len(x_train[0]))
print(x_train[0].shape)
print('Test input shape: ', x_test.shape)
print(len(x_test))
print(len(x_test[0]))
print(x_test[0].shape)

# classifiying with tf.keras RNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim = vocab_size + 1, output_dim = 16),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units = 16, dropout = 0.2, recurrent_dropout = 0.0)),
    tf.keras.layers.Dense(884, activation = 'softmax')
]
)

# compile model
model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer = 'Adam',
              metrics = ['acc'])

model.summary()

# test model
history = model.fit(x = x_train, y = y_train,
        epochs = 50,
        batch_size = 50,
        validation_split = 0.2,
        class_weights = weights
    )

# save model
model.save('drug_review_rnn_50.h5')

# model results
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

fig, (ax0, ax1) = plt.subplots(2, 1)
fig.suptitle('Model Results')
ax0.plot(epochs, acc, 'bo', label = 'Training Accuracy')
ax0.plot(epochs, val_acc, 'b', label = 'Validation Accuracy')
ax0.set_title('Training and Validation Accuracy')
ax0.legend()

ax1.plot(epochs, loss, 'bo', label = 'Training Loss')
ax1.plot(epochs, val_loss, 'b', label = 'Validation Loss')
ax1.set_title('Training and Validation Loss')
ax1.legend()

# load saved model
model = tf.keras.models.load_model('drug_review_rnn_50.h5')

# model performance
predictions = model.predict(x_test)

# build confusion matrix
def plot_cm(y_true, y_pred, figsize = (10,10)):
    cm = confusion_matrix(y_true, y_pred, labels = np.unique(y_true))
    cm_sum = np.sum(cm, axis = 1, keepdims = True)
    cm_perc = cm / cm_sum.astype(float) * 100
    annot = np.empty_like(cm).astype(str)
    nrows, ncols = cm.shape
    for i in range(nrows):
        for j in range(ncols):
            c = cm[i, j]
            p = cm_perc[i, j]
            if i == j:
                s = cm_sum[i]
                annot[i, j] = '%.1f%%\n%d/%d' % (p, c, s)
            elif c == 0:
                annot[i, j] = ''
            else:
                annot[i, j] = '%.1f%%\n%d' % (p, c)
    cm = pd.DataFrame(cm, index = np.unique(y_true), columns = np.unique(y_true))
    cm.index.name = 'Actual'
    cm.columns.name = 'Predicted'
    fig, ax = plt.subplots(figsize = figsize)
    sns.heatmap(cm, cmap= "YlGnBu", annot = annot, fmt = '', ax = ax)

plot_cm(y_test.argmax(axis = 1), predictions.argmax(axis = 1), figsize = (30,30))

# model accuracy
accuracy_metric = accuracy_score(y_test, predictions)

print('Accuracy: ', accuracy_metric)

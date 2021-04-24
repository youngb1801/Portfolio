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


# load data
train_df = pd.read_csv('/Users/bretyoung/Documents/GitHub/DSC_680_data/drugsCom_raw/drugsComTrain_raw.tsv', sep = '\t')
test_df = pd.read_csv('/Users/bretyoung/Documents/GitHub/DSC_680_data/drugsCom_raw/drugsComTest_raw.tsv', sep = '\t')

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
condition_counts = train_df['conditions'].value_counts()
print(condition_counts)

# visualiztions
fig, ax = plt.subplots(1, 1)
ax = sns.countplot(x = "condition", data = train_df)
fig.set_title('Distribution of Conditions')
fig.show()

# set data and labels
x_train = train_df['review']
x_test = test_df['review']
y_train = train_df['condition']
y_test = test_df['condition']

# labels to binary class matrix
y_train = y_train.numpy() # tf.keras.utils.to_categorical(y_train, num_classes = (len(condition_counts) + 1), dtype = 'float32')
y_test = y_test.numpy() # tf.keras.utils.to_categorical(y_test, num_classes = (len(condition_counts) + 1), dtype = 'float32')

# vectorize text
vocab_size = 1000
encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens = vocab_size)
x_train = encoder.adapt(x_train.batch(64))
x_test = encoder.adapt(x_test.batch(64))


# pad_sequence
review_len_max = 500
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen = review_len_max)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen = review_len_max)

print('Training input shape: ', x_train.shape)
print('Test input shape: ', x_test.shape)

# classifiying with tf.keras RNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim = review_len_max, output_dim = 128),
    tf.keras.layers.LSTM(units = 128),
    tf.keras.layers.Dense(, activation = 'softmax')

]
)

# compile model
model.compile(loss = tf.keras.losses.CategoricalCrossentropy(),
              optimizer = tf.keras.optimizers.Adam,
              metrics = ['acc'])

model.summary()

# test model
history = model.fit(x = x_train, y = y_train,
        epochs = 10,
        batch_size = 128,
        validation_split = 0.25
    )

# save model
model.save('drug_review_rnn.h5')

# model results
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)

fig, (ax0, ax1) = plt.subplots(2, 1)
fig.suptitle('Model Results')
ax0.plot(epochs, acc, 'bo', label = 'Training Accuracy')
ax0.plot(epochs, val_acc, 'bo', label = 'Validation Accuracy')
ax0.set_title('Training and Validation Accuracy')
ax0.legend()

ax1.plot(epochs, loss, 'bo', label = 'Training Loss')
ax1.plot(epochs, val_loss, 'bo', label = 'Validation Loss')
ax1.set_title('Training and Validation Loss')
ax1.legend()

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

plot_cm(y_test.values.argmax(axis = 1), predictions.values.argmax(axis = 1))

# Accuracy : the proportion of the total number of predictions that were correct.
# Positive Predictive Value or Precision : the proportion of positive cases that were correctly identified.
# Negative Predictive Value : the proportion of negative cases that were correctly identified.
# Sensitivity or Recall : the proportion of actual positive cases which are correctly identified.
# Specificity : the proportion of actual negative cases which are correctly identified

# F1 score

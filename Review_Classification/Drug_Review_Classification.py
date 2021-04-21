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
VOCAB_SIZE = 1000
encoder = tf.keras.layers.experimental.preprocessing.TextVectorization(
    max_tokens=VOCAB_SIZE)
x_train = encoder.adapt(x_train.batch(64))
x_test = encoder.adapt(x_test.batch(64))


# pad_sequence
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen = 500)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen = 500)

print('Training input shape: ', x_train.shape)
print('Test input shape: ', x_test.shape)

# classifiying with tf.keras RNN

# save model

# test models

# model performance

# build confusion matrix

# Accuracy : the proportion of the total number of predictions that were correct.
# Positive Predictive Value or Precision : the proportion of positive cases that were correctly identified.
# Negative Predictive Value : the proportion of negative cases that were correctly identified.
# Sensitivity or Recall : the proportion of actual positive cases which are correctly identified.
# Specificity : the proportion of actual negative cases which are correctly identified

# F1 score

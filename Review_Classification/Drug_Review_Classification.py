#!/usr/local/bin/python3

# load required packages
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',100)
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')
from keras.preprocessing import sequence
from keras import models
from keras import layers


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



# visualiztions
fig, ax = plt.subplots(1, 1)
ax = sns.countplot(x = "condition", data = train_df)
fig.set_title('Distribution of Conditions')
fig.show()

# unbalanced classes

# classifiying with keras RNN

# test models

# model performance

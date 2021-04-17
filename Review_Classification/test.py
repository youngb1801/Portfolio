#!/usr/local/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv('/Users/bretyoung/Documents/GitHub/DSC_680_data/drugsCom_raw/drugsComTrain_raw.tsv', sep = '\t')

for i in train_df.columns:
    print(i)


fig, ax = plt.subplots(1, 1)
ax = sns.countplot(x = "condition", data = train_df)
fig.show()

import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())

X = df.iloc[:, :-1]
y = df.iloc[:, -1]


df_fill = df.copy()
num_cols = df_fill.select_dtypes(include=np.number).columns
df_fill[num_cols] = df_fill[num_cols].fillna(df_fill[num_cols].mean())

print(df_fill.isnull().sum())

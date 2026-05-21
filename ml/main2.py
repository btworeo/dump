# ==============================
# Data Preprocessing Example
# Fixed & Improved Version
# ==============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# ==============================
# Load Dataset
# ==============================

try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: data.csv file not found.")
    exit()

# ==============================
# Display Dataset
# ==============================

print("\n===== FULL DATASET =====")
print(df)

# ==============================
# Dataset Information
# ==============================

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe(include='all'))

# ==============================
# Check Missing Values
# ==============================

print("\n===== NULL VALUES =====")
print(df.isnull())

print("\n===== NULL VALUE COUNT =====")
print(df.isnull().sum())

# ==============================
# Separate Features & Target
# ==============================

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

print("\n===== FEATURES (X) =====")
print(X)

print("\n===== TARGET (y) =====")
print(y)

# ==============================
# Method 1: Remove Missing Rows
# ==============================

df_dropna = df.copy()

print("\n===== DROP NULL ROWS =====")
print("Before:", df_dropna.shape)

df_dropna.dropna(inplace=True)

print("After :", df_dropna.shape)

# ==============================
# Method 2: Fill Missing Values
# ==============================

df_fillna = df.copy()

# Select numeric columns only
numeric_cols = df_fillna.select_dtypes(include=np.number).columns

# Fill numeric null values with mean
df_fillna[numeric_cols] = df_fillna[numeric_cols].fillna(
    df_fillna[numeric_cols].mean()
)

# Fill categorical columns with mode
categorical_cols = df_fillna.select_dtypes(exclude=np.number).columns

for col in categorical_cols:
    df_fillna[col].fillna(df_fillna[col].mode()[0], inplace=True)

print("\n===== AFTER FILLING NULL VALUES =====")
print(df_fillna.isnull().sum())

# ==============================
# Final Processed Dataset
# ==============================

print("\n===== CLEANED DATASET =====")
print(df_fillna)

# ==============================
# Optional Visualization
# ==============================

# Histogram for numeric columns
df_fillna.hist(figsize=(10, 8))

plt.tight_layout()
plt.savefig("histogram2.png")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

hs = fetch_california_housing(as_frame=True)

df = hs.frame

print(df.head())
print("Shape: ", df.shape)
print("Rows: ", df.shape[0])
print("Columns: ", df.shape[1])
print("Total Elements: ", df.size)
print("Info: ")
print(df.info())

plt.scatter(df["HouseAge"], df["MedHouseVal"])
plt.title("House Age vs. Median House Value")
plt.xlabel("House Age")
plt.ylabel("Median House Value")
plt.savefig('scatterb.png')

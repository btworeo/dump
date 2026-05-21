import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
df.isnull().sum()
df.drop(['Pregnancies'], axis=1, inplace=True)
X = df
y = df["Outcome"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X["Outcome"] = le.fit_transform(X["Outcome"])
y = le.fit_transform(y)

cols = X.columns

from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X = ms.fit_transform(X)
X = pd.DataFrame(X, columns=cols)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_

correct_labels = np.sum(y == labels)
correct_labels
print("Result %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print("Accuracy score: {0:0.2f}".format(correct_labels / y.size))

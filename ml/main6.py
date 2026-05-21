import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
dataset = pd.read_csv('diabetes.csv')

# Features and target
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(dataset.head())

# Split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=0
)

print("X_train:\n", X_train)
print("y_train:\n", y_train)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)  # Avoid data leakage

print("Scaled X_train:\n", X_train)

# Train KNN model
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

# Predictions
y_pred = knn.predict(X_test)

# Metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Class 0", "Class 1"]
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix (k=5)")
plt.grid(False)
plt.savefig("m6.png")

# Classification Report
print("\nClassification Report:\n")

print(classification_report(
    y_test,
    y_pred,
    target_names=["Class 0", "Class 1"]
))

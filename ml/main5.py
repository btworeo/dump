import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ML imports
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score
)

# Load dataset
pima = pd.read_csv('diabetes.csv')

# Display first 5 rows
print(pima.head())

# Features and target
X = pima.drop("Outcome", axis=1)
y = pima["Outcome"]

print("X shape:", X.shape)
print("y shape:", y.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1
)

# Create Logistic Regression model
logreg = LogisticRegression(
    random_state=16,
    max_iter=1000
)

# Train model
logreg.fit(X_train, y_train)

# Predict
y_pred = logreg.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Confusion Matrix
cnf_matrix = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
class_names = [0, 1]

fig, ax = plt.subplots(figsize=(6, 5))

sns.heatmap(
    pd.DataFrame(cnf_matrix),
    annot=True,
    cmap="YlGnBu",
    fmt='g'
)

ax.xaxis.set_label_position("top")

plt.title('Confusion Matrix', y=1.1)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')

plt.xticks(np.arange(len(class_names)) + 0.5, class_names)
plt.yticks(np.arange(len(class_names)) + 0.5, class_names)

plt.tight_layout()
plt.savefig('confusion_matrix1.png')

# Classification report
target_names = ['without diabetes', 'with diabetes']

print("\nClassification Report:\n")
print(classification_report(
    y_test,
    y_pred,
    target_names=target_names
))

import numpy as py
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
dataset = pd.read_csv("datanew.csv")
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
#Training and Testing Data (divide the data into two part)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)
#regression
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train,y_train)

#for predict the test values
y_pred=reg.predict(X_test)

#Visualize the Traing data
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train, reg.predict(X_train), color='blue')
plt.title("linear Regression Salary Vs Experience")
plt.xlabel("Years of Employee")
plt.ylabel("Saleries of Employee")
plt.savefig("linear_regression_plot1.png")
#Visualize the testing data
plt.scatter(X_test,y_test,color='red')
plt.plot(X_test, reg.predict(X_test), color='blue')
plt.title("linear Regression Salary Vs Experience")
plt.xlabel("Years of Employee")
plt.ylabel("Saleries of Employee")
plt.savefig("linear_regression_plot2.png")
mse = mean_squared_error(y_test, y_pred) # Calculate Mean Squared Error
r2 = r2_score(y_test, y_pred) # Calculate R² Score
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

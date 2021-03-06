# support vector regression by 2blam

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# import dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values # 2nd column
y = dataset.iloc[:, 2].values # 3rd column

# split into training and testing dataset
"""
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0) # 20% for testing dataset
"""

# re-scale feature values
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X= sc_X.fit_transform(X)
y= sc_y.fit_transform(y)

# fit the support vector regression model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = "rbf") #gaussian
regressor.fit(X, y)

# predict 
# 1) transform the level to the corresponding scale
# 2) fit into the regressor
# 3) inverse transform the scaled value to the actual scale
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# plot
plt.scatter(X, sc_y.inverse_transform(y), color="red")
plt.plot(X, sc_y.inverse_transform(regressor.predict(X)), color="blue")
plt.title("Position Level vs Salary (Support vector regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()      

# smoother curve
X_grid = np.arange(min(X), max(X), 0.1) 
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, sc_y.inverse_transform(y), color="red")
plt.plot(X_grid, sc_y.inverse_transform(regressor.predict(X_grid)), color="blue")
plt.title("Position Level vs Salary (Support vector regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()
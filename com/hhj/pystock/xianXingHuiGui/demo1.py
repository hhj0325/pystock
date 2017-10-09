import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()



data = pd.read_csv('d:\pyworkspace\pystock\CCPP\ccpp.csv')
print(data.head())
print(data.shape)

X = data[['AT', 'V', 'AP', 'RH']]
print(X.head())

y = data[['PE']]
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

linreg = LinearRegression()
linreg.fit(X_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)
# PE=447.06297099-1.97376045*AT-0.23229086*V+0.0693515*AP-0.15806957*RH

# 模型拟合测试集
y_pred = linreg.predict(X_test)
# 用scikit-learn计算MSE
print("MSE:", metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

X = data[['AT', 'V', 'AP', 'RH']]
y = data[['PE']]
predicted = cross_val_predict(linreg, X, y, cv=10)
# 用scikit-learn计算MSE
print("MSE:", metrics.mean_squared_error(y, predicted))
# 用scikit-learn计算RMSE
print("RMSE:", np.sqrt(metrics.mean_squared_error(y, predicted)))


fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()















"""
以下是一组用于回归的方法，他们的目标值是输入变量的线性组合。假设数学符号 表示预测值。
在整个模块中，我们指定coef_ 代表向量, intercept_ 代表w_0 。
"""
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 2, 10])
print(reg.coef_)
print(reg.intercept_)


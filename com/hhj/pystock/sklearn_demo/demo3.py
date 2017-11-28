"""
默认内核rbf首先被改变到linear估计器被构造之后SVC()，
并且改回到rbf重新设计估计器并进行第二预测。
"""
import numpy as np
from sklearn.svm import SVC

rng = np.random.RandomState(0)
X = rng.rand(100, 10)
y = rng.binomial(1, 0.5, 100)
X_test = rng.rand(5, 10)

clf = SVC()
# 默认内核rbf
clf.fit(X, y)
print(clf.predict(X_test))
# 修改内核为linear
clf.set_params(kernel='linear').fit(X, y)
print(clf.predict(X_test))

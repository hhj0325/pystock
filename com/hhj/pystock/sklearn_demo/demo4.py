import numpy as np

from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer


X = np.array([[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]])
y = np.array([0, 0, 1, 1, 2])
y_name = np.array(["zero", "one", "two"])
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
print("--原始y--\n", y)
print("--预测集--\n", classif.fit(X, y).predict(X))
print("--预测集（带名称）--\n", classif.fit(X, y_name[y]).predict(X))

y = LabelBinarizer().fit_transform(y)
print("--原始y--\n", y)
# 第四个和第五个实例返回所有零，表示它们不匹配三个标签之一fit。
print("--预测集--\n", classif.fit(X, y).predict(X))

y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
print("--原始y--\n", y)
print("--预测集--\n", classif.fit(X, y).predict(X))


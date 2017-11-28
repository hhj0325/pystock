"""
第一个predict()返回一个整数数组，因为iris.target 使用了一个整数数组fit。
第二个predict()返回一个字符串数组，因为iris.target_names是用于拟合。
"""
from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
clf = SVC()
# 分类
clf.fit(iris.data, iris.target)
# 预测
print(list(clf.predict(iris.data[:3])))
print(list(clf.predict(iris.data[-3:])))

# 输出花名
print(iris.target_names[:])
# 分类
clf.fit(iris.data, iris.target_names[iris.target])
# 预测
print(list(clf.predict(iris.data[:3])))
print(list(clf.predict(iris.data[-3:])))

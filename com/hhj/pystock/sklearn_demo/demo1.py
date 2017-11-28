"""
输入：像素点阵的数组
输出：预测数字
"""
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
# 数字样本
print(digits.data)

# 数字数据集的真实数据
print(digits.target)

# sklearn.svm.SVC实现支持向量分类的类
clf = svm.SVC(gamma=0.001, C=100.)
# 从模型中学习。这是通过将我们的训练集传递给该fit方法来完成的。
# 作为一个训练集，让我们使用除最后一个数据集的所有图像。
clf.fit(digits.data[:-1], digits.target[:-1])
# 预测新值
clf.predict(digits.data[-1:])

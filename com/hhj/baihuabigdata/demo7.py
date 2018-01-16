"""
page 163
"""
from sklearn import svm

X = [
    [34],
    [33],
    [32],
    [31],
    [31],
    [30],
    [25],
    [23],
    [22],
    [18]
]

y = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

clf = svm.SVC(kernel='rbf').fit(X, y)
p = [[37]]
print(clf.predict(p))

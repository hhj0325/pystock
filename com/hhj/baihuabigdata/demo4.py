"""
page 132
"""
from sklearn.naive_bayes import GaussianNB

data_table = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

X = [x[0:2] for x in data_table]
print(X)
y1 = [x[2] for x in data_table]
print(y1)
clf1 = GaussianNB().fit(X, y1)
p1 = [[1, 0]]
print(clf1.predict(p1))

y2 = [x[3] for x in data_table]
print(y2)
clf2 = GaussianNB().fit(X, y2)
p2 = [[1, 0]]
print(clf1.predict(p2))

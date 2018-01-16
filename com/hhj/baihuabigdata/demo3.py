"""
page 130
"""
from sklearn.naive_bayes import GaussianNB

data_table = [["date", "weather"],
              [1, 0],
              [2, 1],
              [3, 2],
              [4, 1],
              [5, 2],
              [6, 0],
              [7, 0],
              [8, 3],
              [9, 1],
              [10, 1],
              ]

X = [[x[1]] for x in data_table[1:]]
y = [x[1] for x in data_table[2:]]
# y后面添加一个数。不然fit会有bug。
y.append(1)

print(X)
print(y)

clf = GaussianNB().fit(X, y)
p = [[1]]
print(clf.predict(p))

"""
page 93
"""
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [0.199, 0.389, 0.580, 0.783, 0.980, 1.177, 1.380, 1.575, 1.771]

A = np.vstack([x, np.ones(len(x))]).T
print(A)

a, b = np.linalg.lstsq(A, y)[0]
print("a=" + str(a) + ", b=" + str(b))

x = np.array(x)
y = np.array(y)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, a * x + b, 'r', label='Fitted line')
plt.show()

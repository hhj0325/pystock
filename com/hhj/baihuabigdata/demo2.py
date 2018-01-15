"""
page 103
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

T = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968]
S = [29.72, 30.61, 31.51, 32.13, 32.34, 32.85, 33.56, 34.20, 34.83]

xdata = np.array(T)
ydata = np.log(np.array(S))

def func(x, a, b):
    return a + b * x

popt, pcov = curve_fit(func, xdata, ydata)
print(popt)
print(pcov)

plt.plot(xdata, ydata, 'ko', label="Original Noised Data")
plt.plot(xdata, func(xdata, *popt), 'r', label="Fitted Curve")
plt.show()

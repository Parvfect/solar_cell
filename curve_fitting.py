import numpy as np
from scipy.optimize import curve_fit
import scipy as sp
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


x = list(range(1,100))
y = [math.exp(i) for i in x]


def objective(x, a, b):
    return a*x + b


def curve_fitting(x, y):
    popt, pcov = curve_fit(objective, x, y, bounds = [-np.inf, np.inf])
    a, b = popt
    y1 = [objective(i, a, b) for i in x]
    return y1, a, b

"""
t = curve_fitting(x, y)
y1 = [objective(i, t[0], t[1]) for i in x]
plt.plot(x, y, 'o')
plt.plot(x, y1)
plt.show()
"""
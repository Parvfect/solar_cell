import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math

# Ideality factor - 3.64

q = 1.602176634e-19
T = 300
kb = 1.38e-23

def standard_error(y_arr):
    return np.std(y_arr)/math.sqrt(len(y_arr))
def get_boltzmann(a, b):
    return -(q*b)/(a*T*2.54) 

df = pd.read_excel("scd.xlsx")


x = df["V2"]
y = df["I2"]
print(standard_error(y))
plt.plot(x, y, color = 'blue')
plt.grid()
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.ylabel("Current (A) +/- 1.85 A")
plt.title("IV curve of Solar Cell under dark conditions")
plt.errorbar(x, y, yerr=standard_error(y),  ecolor = 'red', alpha=0.5, capsize=2)
plt.show()

uncertainty_y = standard_error(y) + 0.02


y = [i for i in y if i>0]
x = x[(len(x) - len(y)):]
print(y)
y = [math.log((i*math.pow(10,-3))) for i in y]

y1, a, b = curve_fitting(x, y)


plt.plot(x,y, 'o')
plt.plot(x, y1)
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.errorbar(x,y,xerr=0.01, yerr=0.01, fmt='o')
plt.title("ln(I) vs V")
plt.show()

print("Saturation Current - {}".format(-b/100))
print("Ideality Factor - {}".format((-q * b)/(kb* T * a)/100))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math

#1.84 for the whole - 1.43 for the most linear part of the curve

q = 1.602176634e-19
T = 298
kb = 1.38e-23

def standard_error(y_arr):
    return np.std(y_arr)/math.sqrt(len(y_arr))
def get_boltzmann(a, b):
    return -(q*b)/(a*T*2.54*100) 

df = pd.read_excel("boltz.xlsx")
names = list(df)
x = df[names[0]]
y = df[names[1]]

#uncertainty_y = standard_error(y) + 0.02

y = [i for i in y if i>=0]
x = x[7:9]
y = y[:2]
y = [math.log((i*math.pow(10,-3))) for i in y]

y1, a, b = curve_fitting(x, y)

plt.plot(x,y, 'o', label="Orignal Curve")
plt.plot(x, y1, label="Fitted Linear Function")
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.ylabel("ln(I)")
#plt.errorbar(x,y,xerr=0.01, yerr=0.01, fmt='o')
plt.legend()
plt.title("Curve Fitting to the most linear part of the IV Curve")
plt.show()

sb = get_boltzmann(a,b)
print(sb)

#print("Saturation Current - {}".format(-b/100))
#print("Ideality Factor - {}".format((-q * b)/(kb* T * a)/100))
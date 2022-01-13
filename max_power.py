import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math

q = 1.602176634e-19
T = 298
kb = 1.38e-23

def get_boltzmann(a, b):
    return -(q*b)/(a*T*2.54) 

df = pd.read_excel("scl.xlsx")

print(df["I2"])

x = df["V2"][:32]
y = df["I2"][:32]
power =  []
x = x.tolist()
y = y.tolist()

lowPow = 12
for i in range(len(x)):
    tp = x[i]*y[i]
    if tp < 0:
        if abs(tp) < lowPow:
            lowPow = abs(tp)
    power.append(x[i]*y[i])
    

plt.plot(x, power)
plt.grid()
plt.title("Determining Max Power {}e-3 W".format(lowPow))
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.ylabel("Power (W) +/- 0.02 W")
plt.errorbar(x, power, yerr=0.02, xerr=0.01, fmt = 'o')
plt.show()

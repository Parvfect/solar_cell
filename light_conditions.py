
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_excel("scl.xlsx")
I1 = df["I2"][:35]
I2 = df["I2D"][:35]
V2 = df["V2"][:35]


def standard_error(y_arr):
    return np.std(y_arr)/math.sqrt(len(y_arr))


error = (standard_error(I2) + standard_error(I1))/2
plt.plot(V2, I1, label = "Light Conditions")
plt.plot(V2, I2, label = "Dark Conditions")
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.ylabel("Current (A) +/- 0.01 A")
#plt.errorbar(V2, I2, yerr=standard_error(I2), ecolor = 'red', alpha=0.5, capsize=2)
#plt.errorbar(V2, I1, yerr=standard_error(I1), ecolor = 'red', alpha=0.5, capsize=2)
plt.legend()
plt.grid()
plt.title("IV curve of Solar Cell under varying conditions")
plt.show()
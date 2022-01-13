import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from curve_fitting import curve_fitting, objective
import math
# The gradient between V = 0 and I = 0 
# Let's load some data from the file
q = 1.602176634e-19
T = 298
kb = 1.38e-23

def get_boltzmann(a, b):
    return -(q*b)/(a*T*2.54) 

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

df = pd.read_excel("scl.xlsx")

x = df['V2'].tolist()
y = df['I2'].tolist()
print(y)
x1 = []
y1 = []
i0 = 0

# We need to find the gradient between V = 0 and I = 0
for i in range(len(x)):
    if y[i] > 0:
        i0 = i
        break

x1 = x[:i0]
y1 = y[:i0]


# Now we fit this to a line
y2 = [sign(i)*math.log(abs(i)*math.pow(10,-3)) for i in y1]


y3, a, b = curve_fitting(x1[:22], y2)
plt.plot(x1[:22],y2, 'o')
plt.plot(x1[:22],y3)
plt.xlabel("Voltage (V) +/- 0.01 V")
#plt.errorbar(x,y,xerr=0.01, yerr=0.01, fmt='o')
plt.title("ln(I) vs V")
plt.show()

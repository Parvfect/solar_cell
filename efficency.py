import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import simps
from numpy import trapz

q = 1.602176634e-19
T = 298
kb = 1.38e-23
A = 70 * 50 * 1e-6

df = pd.read_excel("scl.xlsx")
lux = 2780

def get_max_power(voltage_arr, current_arr):
    """ 
    Finds the maximum power of light IV curve of diode, returns max power and power series
    """
    V = voltage_arr
    I = current_arr
    P = [a * b for a, b in zip(V, I)]
    Pmax = max([abs(i) for i in P])
    return Pmax, P

def find_fill_factor(I, dx):
    """
    Finds fill factor of light IV curve of the points I<0
    """
    return - simps(I, dx=dx) 

def convert_lux(val):
    return val * 8e-3


I = [x for x in df["I2"] if x <= 1]
V = df["V2"][:len(I)]

plt.plot(V, I, label = "Light Conditions")
#plt.plot(V2, I2, label = "Dark Conditions")
plt.xlabel("Voltage (V) +/- 0.01 V")
plt.ylabel("Current (mA) +/- 0.01 mA")
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#plt.errorbar(V2, I2, yerr=standard_error(I2), ecolor = 'red', alpha=0.5, capsize=2)
#plt.errorbar(V2, I1, yerr=standard_error(I1), ecolor = 'red', alpha=0.5, capsize=2)
#plt.legend()
plt.grid()
plt.title("Estimating Efficiency of Solar Cell using Fill Factor and Power")

Pmax, P = get_max_power(V, I)
print(I)
fill_factor = find_fill_factor(I, 0.2)
V_o = V[len(V) - 2]
I_o = I[0]
print(I[0])
ISC = (I[0], V[0])
VOC = (V[len(V) - 2], I[len(I) - 2])
i = [0, 5.2, 3.8]
j = [-1.71, 0, -1.68]

FF = r'$FF = \frac{I_{max}V_{max}}{I_{SC}V_{OC}}$'
Pmax_ = r'$P_{max} = I_{max}V_{max}$'
plt.scatter(i, j, color = 'red')
plt.annotate("ISC", (i[0], j[0]), fontfamily = 'montserrat', fontsize = 10)
plt.annotate("VOC", (i[1], j[1]), fontfamily = 'montserrat', fontsize = 10)
plt.annotate(Pmax_, (i[2], j[2]), fontfamily = 'montserrat', fontsize = 10)
#plt.annotate("Voc", VOC, xytext=(VOC[0] + 0.1, VOC[1] + 0.1), arrowprops=dict(facecolor='black', shrink=1))
#plt.annotate("Isc", ISC)
plt.fill_between(V[:-1], I[:-1], 0, color = 'black', alpha = 0.2)
plt.text(2, -0.75, FF, fontfamily = 'LiSong Pro', fontsize = 15)
plt.show()

efficency = Pmax / (A * convert_lux(lux)) * 0.1
efficency_2 = fill_factor/ (A * convert_lux(lux)) * 0.1
print("Efficency: ", efficency)
print("Efficency 2: ", efficency_2)


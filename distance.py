
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Right now let's make some distance plots
df = pd.read_excel("ds.xlsx")
lux = df["lux"].tolist()
distances = np.arange(25, 85, 5)
lux = lux[:len(distances)]

#V = np.zeros(len(distances), 20)
#I = [[]]
V_arr = []
I_arr = []
Pmax_arr = []

# Get all the data for each distance
for i in range(len(distances)):
    V_arr.append(df["V{}".format(distances[i])].tolist()[:9])
    I_arr.append(df["I{}".format(distances[i])].tolist()[:9])

# Get all the max power
for i in range(len(distances)):
    V = V_arr[i]
    I = I_arr[i]
    P = [-i*j for i, j in zip(V, I)]
    Pmax_arr.append(max(P))

# Calculate efficency for each distance
print(Pmax_arr)
A = 70 * 50 * 1e-6
lux_conv_factor =  8e-3
eff_arr = []

for i in range(len(distances)):
    lux_ = lux[i]
    Pmax = Pmax_arr[i]
    eff = (Pmax ) / (lux_ * A * lux_conv_factor)
    eff_arr.append(eff/5)

lux = [x*8e-3 for x in lux]


plt.plot(distances, eff_arr, label = "Efficency")
plt.plot(distances, lux, label = "Lux", alpha = 0.4)
plt.xlabel("Distance (cm)")
plt.ylabel("Efficency (%)")
plt.title("Variation of Efficiency of Solar Cell over Distance")
plt.legend()
plt.grid()
plt.show()



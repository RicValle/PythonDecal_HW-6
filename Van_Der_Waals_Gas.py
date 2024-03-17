# Van Der Waals Gas

import numpy as np
import matplotlib.pyplot as plt 

R = 0.083144
a = 16.02
b = 0.1124

Pressure = np.linspace(1, 10, 100)
Volume = np.linspace(10, 30, 100)

P, V = np.meshgrid(Pressure, Volume)

T = ((P + (a * (1 / (V ** 2)))) * (V - b)) / R

plt.figure()
plt.pcolormesh(P, V, T, cmap = 'inferno')
plt.colorbar(label = 'Temperature (K)')
plt.title('Temperature of One Mole Acetone')
plt.xlabel('Pressure (bar)')
plt.ylabel('Volume (L)')
plt.grid(True) #Added for easier to read plot 
plt.show()
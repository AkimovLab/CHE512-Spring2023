import numpy as np
import matplotlib.pyplot as plt

# Reading data
filename = "output.txt"
data = np.loadtxt(filename, skiprows=1)
T, X, P, E_pot, E_kin, E_tot = data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4], data[:, 5]

# phase space diagram
plt.figure()
plt.plot(X, P)
plt.xlabel("Position")
plt.ylabel("Momentum")
plt.title("Phase Space Diagram")

# the energies
plt.figure()
plt.plot(T, E_tot, label="Total Energy")
plt.plot(T, E_pot, label="Potential Energy")
plt.plot(T, E_kin, label="Kinetic Energy")
plt.xlabel("Time")
plt.ylabel("Energy")
plt.title("Energies")
plt.legend()

plt.show()


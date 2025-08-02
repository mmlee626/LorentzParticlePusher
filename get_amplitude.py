import matplotlib.pyplot as plt
import numpy as np
import os

filename = f"trajectory0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, xpos, ypos, zpos = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

maxima = []
minima = []
data = ypos
avg = np.mean(data)
for i in range(1, len(data) - 1):
    if data[i] >= data[i - 1] and data[i] > data[i + 1] and data[i] > avg:
        maxima.append(data[i])
    elif data[i] <= data[i - 1] and data[i] < data[i + 1] and data[i] < avg:
        minima.append(data[i])
amplitude = np.mean(maxima) - np.mean(minima)
std_dev = 0.5 * np.sqrt(np.std(maxima)**2 + np.std(minima)**2)
print(f"Amplitude: {amplitude}")
print(f"Radius: {amplitude / 2}")
print(f"Std in Radius: {std_dev}")
print(f"Std Percent: {std_dev / (amplitude / 2) * 100:.4f}%")
print(f"Max: {max(data)}")
print(f"Min: {min(data)}")
print(f"Num Periods: {len(maxima)}")

plt.plot(t, data)
plt.title("Particle Trajectories")
plt.xlabel("Time")
plt.ylabel("Y Position")
plt.tight_layout()
plt.show()
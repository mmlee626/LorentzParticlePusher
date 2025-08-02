import matplotlib.pyplot as plt
import numpy as np
import os

filename = f"trajectory0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, xpos, ypos, zpos = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

datas = [xpos, ypos]
for data in datas:
    maxima = []
    minima = []
    avg = np.mean(data)
    for i in range(1, len(data) - 1):
        if data[i] >= data[i - 1] and data[i] > data[i + 1] and data[i] > avg:
            maxima.append(data[i])
        elif data[i] <= data[i - 1] and data[i] < data[i + 1] and data[i] < avg:
            minima.append(data[i])
    amplitude = np.mean(maxima) - np.mean(minima)
    print(f"Semi-axis: {amplitude / 2}")
    print(f"Std in Semi-axis: {0.5 * np.sqrt(np.std(maxima)**2 + np.std(minima)**2)}")

    plt.plot(data)
    plt.title("Particle Trajectories")
    plt.xlabel("Time Step")
    plt.ylabel("Position")
    plt.show()
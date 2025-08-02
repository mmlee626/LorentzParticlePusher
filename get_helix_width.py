import matplotlib.pyplot as plt
import numpy as np
import os

filename = f"trajectory0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, xpos, ypos, zpos = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

max_idxs = []
min_idxs = []
data = xpos
avg = np.mean(data)
for i in range(1, len(data) - 1):
    if data[i] >= data[i - 1] and data[i] > data[i + 1] and data[i] > avg:
        max_idxs.append(i)

helix_width = np.mean(np.diff(zpos[max_idxs])) if len(max_idxs) > 1 else 0
print(f"Helix Width: {helix_width}")

plt.plot(data)
plt.title("Particle Trajectories")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.show()
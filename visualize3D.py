import matplotlib.pyplot as plt
import numpy as np
import os

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
colors = ['k', 'r', 'b']
num_particles = 1

for i in range(num_particles):
    filename = f"trajectory{i}.csv"
    if not os.path.exists(filename):
        print(f"{filename} missing")
        continue
    data = np.loadtxt(filename, delimiter=",")
    ax.plot(data[:, 1], data[:, 2], data[:, 3], colors[i])

plt.title("Particle Trajectory")
plt.xlabel("X")
plt.ylabel("Y")
ax.set_zlabel("Z")
plt.show()
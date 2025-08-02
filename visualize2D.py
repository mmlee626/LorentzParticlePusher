import matplotlib.pyplot as plt
import numpy as np
import os

# Plot particle trajectory in 2D
fig = plt.figure()
fig.set_size_inches(6, 6)
ax = fig.add_subplot(111)
colors = ['k', 'r', 'b']
num_particles = 1

for i in range(num_particles):
    filename = f"trajectory{i}.csv"
    if not os.path.exists(filename):
        print(f"{filename} missing")
        continue
    data = np.loadtxt(filename, delimiter=",")
    ax.plot(data[:, 1], data[:, 2], colors[i], label=f'Particle {i}')

plt.title("Particle Trajectory")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()
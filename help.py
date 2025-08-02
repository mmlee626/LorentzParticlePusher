import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1.0
k = np.pi / 2.0
B_conversion = 1.0  # set to match natural unit conversion if needed
E_conversion = 1.0

# Field definitions
def b_field(x, y, z, t):
    r = np.sqrt(x**2 + y**2 + z**2)
    if r == 0:
        return np.array([0.0, 0.0, 0.0])  # avoid division by zero
    B_mag = A / r * (1 + k * t)
    return np.array([0.0, 0.0, B_mag]) * B_conversion

def e_field(x, y, z, t):
    theta = np.array([y, -x, 0])
    norm = np.linalg.norm(theta)
    if norm == 0:
        return np.array([0.0, 0.0, 0.0])  # avoid division by zero
    theta_hat = theta / norm
    E_mag = A * k
    return theta_hat * E_mag * E_conversion

# Grid for plotting
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Time snapshots to plot
time_values = [0.0, 0.5, 1.0, 1.5]

# Plotting loop
fig, axes = plt.subplots(1, len(time_values), figsize=(5 * len(time_values), 5))
if len(time_values) == 1:
    axes = [axes]  # make iterable

for idx, t in enumerate(time_values):
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    Bz = np.zeros_like(X)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            x, y = X[i, j], Y[i, j]
            e = e_field(x, y, 0.0, t)
            b = b_field(x, y, 0.0, t)
            Ex[i, j] = e[0]
            Ey[i, j] = e[1]
            Bz[i, j] = b[2]  # scalar field for Bz

    ax = axes[idx]
    ax.set_title(f"t = {t:.1f}")
    strm = ax.quiver(X, Y, Ex, Ey, color='blue', scale=25)
    contour = ax.contourf(X, Y, Bz, levels=20, cmap='inferno', alpha=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')

cbar = fig.colorbar(contour, ax=axes, shrink=0.8, orientation='horizontal', pad=0.1)
cbar.set_label("Bz Magnitude")
plt.suptitle("Electric Field (arrows) and Magnetic Field Bz (contours)")
plt.tight_layout()
plt.show()

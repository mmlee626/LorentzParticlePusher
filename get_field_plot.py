import numpy as np
import matplotlib.pyplot as plt

# Vector field function
def vector_field(x, y, t):
    theta = np.array([y, -x, 0])  # azimuthal direction in 3D
    norm = np.linalg.norm(theta)
    if norm == 0:
        return np.array([0.0, 0.0])  # avoid division by zero at origin
    theta_hat = theta / norm
    A = 1.0
    k = np.pi / 2.0 
    E_mag = A * k * np.cos(k * t)
    field = theta_hat * E_mag
    return field[:2]  # only return x and y components

# Grid settings
x_vals = np.linspace(-5, 5, 20)
y_vals = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Time at which to evaluate the field
t = 0.0

# Compute vector field
U = np.zeros_like(X)
V = np.zeros_like(Y)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        fx, fy = vector_field(X[i, j], Y[i, j], t)
        U[i, j] = fx
        V[i, j] = fy

# Plot
plt.figure(figsize=(7, 7))
plt.quiver(X, Y, U, V, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"2D Vector Field at t = {t}")
plt.axis('equal')
plt.grid(True)
plt.show()

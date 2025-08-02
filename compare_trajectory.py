import matplotlib.pyplot as plt
import numpy as np
import os

filename = f"trajectory0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, xpos, ypos, zpos = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
data = zpos
data = data - data[0]

c = 299792458.0
m, q, E = 1e-8, 1.0, 1.0  # mass, charge, electric field strength
vx, vy, vz = 0.5*c, 0.7*c, 0.4*c  # initial velocities
g0 = 1 / np.sqrt(1.0 - (vx**2 + vy**2 + vz**2) / c**2)
px = g0 * m * vx
py = g0 * m * vy
pz = g0 * m * vz

# def f(t):
#     return (c / q / E) * (np.sqrt((q * E * t + g0 * m * v0)**2 + m**2 * c**2)
#                           - np.sqrt((g0 * m * v0)**2 + m**2 * c**2))
# def x(t):
#     return (c / q / E) * (np.sqrt((q*E*t)**2 + (g0*m*v0)**2 + (m*c)**2)
#                           - np.sqrt((g0*m*v0)**2 + (m*c)**2))
# def y(t):
#     return (c / q / E) * (g0*m*v0) * np.arcsinh(q*E*t / np.sqrt((g0*m*v0)**2 + (m*c)**2))

def x(t):
    return (c/q/E) * (np.sqrt((px + q*E*t)**2 + py**2 + pz**2 + (m*c)**2)
                          - np.sqrt(px**2 + py**2 + pz**2 + (m*c)**2))

def y(t):
    return (c/q/E) * py * (np.log(np.sqrt((px + q*E*t)**2 + py**2 + pz**2 + (m*c)**2) + q*E*t + px)
                           - np.log(np.sqrt(px**2 + py**2 + pz**2 + (m*c)**2) + px))

def z(t):
    return (c/q/E) * pz * (np.log(np.sqrt((px + q*E*t)**2 + py**2 + pz**2 + (m*c)**2) + q*E*t + px)
                           - np.log(np.sqrt(px**2 + py**2 + pz**2 + (m*c)**2) + px))

pred_time = np.linspace(t.min(), t.max(), len(data))
pred_pos = z(pred_time)

plt.plot(pred_time, pred_pos, label='Prediction', color='orange', linestyle='--')
plt.plot(t, data, alpha=0.6, label='Simulation')
plt.title("Particle Trajectory")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.tight_layout()

# Calculate average percent error
percent_errors = np.zeros(len(data))
for i in range(len(data)):
    if pred_pos[i] != 0:
        percent_errors[i] = abs((data[i] - pred_pos[i]) / pred_pos[i]) * 100
    else:
        percent_errors[i] = 0.0
print(f"Average Percent Error: {np.mean(percent_errors):.3f}%")

plt.show()
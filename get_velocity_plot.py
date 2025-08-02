import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import os

# Plot particle velocity over time
filename = f"velocities0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, vx, vy, vz = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
velocity = np.sqrt(vx**2 + vy**2 + vz**2)

# Perform a sliding window average to smooth the velocity data
# window_size = 40  # Adjust the window size as needed
# velocity = np.convolve(velocity, np.ones(window_size)/window_size, mode='valid')

# Plot the velocity
plt.plot(t, velocity, label='Velocity')
plt.title("Particle Velocity Over Time")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.tight_layout()
plt.show()
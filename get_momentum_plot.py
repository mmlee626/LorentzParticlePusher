import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import os

# Plot particle velocity over time
filename = f"momentums0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, px, py, pz = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
momentum = np.sqrt(px**2 + py**2 + pz**2)

# Perform a sliding window average to smooth the velocity data
# window_size = 40  # Adjust the window size as needed
# velocity = np.convolve(velocity, np.ones(window_size)/window_size, mode='valid')

# Plot the velocity
plt.plot(t, momentum, label='Velocity')
plt.title("Particle Momentum Over Time")
plt.xlabel("Time")
plt.ylabel("Momentum")
plt.tight_layout()
plt.show()

# Print initial and final momentum
print(f"Initial Momentum: {momentum[0]}")
print(f"Final Momentum: {momentum[-1]}")
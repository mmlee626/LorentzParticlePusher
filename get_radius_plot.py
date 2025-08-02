import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import os

filename = f"trajectory0.csv"
if not os.path.exists(filename):
    print(f"{filename} missing")
    exit(0)

data = np.loadtxt(filename, delimiter=",")
t, xpos, ypos, zpos = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
radius = np.sqrt((xpos)**2 + (ypos)**2 + (zpos)**2)
radius = radius

m, q, v0 = 0.938272, 1.0, 0.001
gamma = 1 / np.sqrt(1 - v0**2)
B_func = (t / (200) + 1) * 0.299792458
# B_func = (1.0 + t * (1 / 2.99792458e5)) * 0.299792458
r_pred = gamma * m * v0 / (q * B_func)

# Calculate mean squared difference
mse = np.mean((radius - r_pred)**2)
print(f"Mean Squared Error: {mse}")

# plt.plot(t, r_pred, color='orange', label='Prediction', linestyle='--')
# plt.plot(t, radius, alpha=0.5, label='Simulation')
# plt.plot(t, radius - r_pred, label='Radius Difference')
plt.plot(t, radius)
plt.title("Particle Trajectories")
plt.xlabel("Time")
plt.ylabel("Radius (m)")
# plt.legend()
plt.tight_layout()
plt.show()

print(radius[-1])

data = radius - np.mean(radius)
# Apply FFT to radius data
data_fft = fft(data)
L = len(data)
frequencies = fftfreq(L, t[2] - t[1])

# Print most significant frequency
max_freq_index = np.argmax(np.abs(data_fft[:L//2]))
print(f"Peak freq: {frequencies[max_freq_index]}")
print(f"Dominant period: {1. / frequencies[max_freq_index]}")

# Take the absolute value and normalize by L to get amplitude spectrum
# plt.plot(frequencies[:L//2], 2.0/L * np.abs(data_fft[0:L//2]))
# plt.title('Frequency Domain Spectrum')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# # plt.ylim(0)
# plt.tight_layout()
# plt.show()
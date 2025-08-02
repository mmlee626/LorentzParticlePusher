# LorentzParticlePusher

This project numerically simulates the motion of a charged particle through user-defined electromagnetic fields via the Lorentz force. The C++ core integrates the particle's trajectory, while the Python scripts are for data analysis and visualization.

## Features

- Flexible electromagnetic field definitions (electric and magnetic fields as functions of position and time)
- Particle Pushers:
  - Runge-Kutta 4th order integration (non-relativistic and relativistic)
  - Boris integrator (relativistic)
- Export of trajectory and physical observables to CSV files
- Python tools for visualizing:
  - Trajectories (2D and 3D)
  - Radius, velocity, momentum, energy evolution
  - Elliptical motion analysis

## Project Structure

```bash
├── main.cpp             # Entry point — compile and run to simulate
├── particle.h/.cpp      # Particle class and integrators
├── vec3.h               # 3D vector utility
├── constants.h          # Physical constants and configuration
├── *.csv                # Generated output data
├── *.py                 # Plotting and analysis scripts

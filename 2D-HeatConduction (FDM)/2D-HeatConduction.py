# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:22:04 2023

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 20  # Dimension in meters
k = 1   # Thermal conductivity in W/m⋅˚C
N = 21  # Number of grid points in each direction (including boundary points)
dx = A / (N - 1)  # Grid spacing

# Create a 2D array to store temperature values
T = np.zeros((N, N))

# Von Neumann boundary conditions
T[:, 0] = 30  # Left boundary at 0˚C
T[:, -1] = 30   # Right boundary at 20˚C
T[0, :] = 80   # Top boundary at 50˚C
T[-1, :] = 30  # Bottom boundary at 75˚C

# Main FDM iteration loop
max_iterations = 10000
tolerance = 1e-6
iteration = 0
converged = False

# for iteration in range(max_iterations):
#     T_new = T.copy()
#     for i in range(1, N - 1):
#         for j in range(1, N - 1):
#             T_new[i, j] = 0.25 * (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1])
    
#     # Check for convergence
#     if np.max(np.abs(T_new - T)) < tolerance:
#         T = T_new
#         break
    
#     T = T_new
while not converged and iteration < max_iterations:
    T_new = T.copy()
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            T_new[i, j] = 0.25 * (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1])
    
    # Check for convergence
    max_change = np.max(np.abs(T_new - T))
    if max_change < tolerance:
        converged = True
    
    T = T_new
    iteration += 1
print(iteration)
print(T_new)
# Plot the temperature distribution
plt.imshow(T, origin='upper', extent=(0, A, 0, A), cmap='hot')
plt.colorbar(label='Temperature (˚C)')
plt.xlabel('X (meters)')
plt.ylabel('Y (meters)')
plt.title('2D Heat Conduction (Steady-State) with Von Neumann Boundary Conditions')
plt.grid(True)
plt.show()

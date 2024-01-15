# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:56:35 2023

@author: ASUS
"""

#Python Code: Decay chain 3-Nuclide / Agung Kurniawan (10219068)

import numpy as np
import matplotlib.pyplot as plt

#Main Parameters
codename = 'Euler-MidPoint'

N_A0 = 147
N_B0 = 0.1*N_A0
N_C0 = 0.25*N_A0
lambda_A = 0.17
lambda_B = 0.25*lambda_A
lambda_C = 0.35*lambda_A
t_final = 50
partitions = 50

#Array of parameters
time = np.linspace(0,t_final,partitions)
dt = time[1] - time[0]
N_A = np.zeros(partitions)
N_B = np.zeros(partitions)
N_C = np.zeros(partitions)
N_A[0] = N_A0
N_B[0] = N_B0
N_C[0] = N_C0

#Main Calculations Start (Modified-Euler Method)
for i in range(0, partitions-1):
    N_A_mid = N_A[i] - lambda_A*N_A[i]*0.5*dt
    N_B_mid = N_B[i] + (-lambda_B*N_B[i] + lambda_A*N_A[i])*0.5*dt
    N_C_mid = N_C[i] + (-lambda_C*N_C[i] + lambda_B*N_B[i])*0.5*dt
    N_A[i+1] = N_A[i] - lambda_A*N_A_mid*dt
    N_B[i+1] = N_B[i] + (-lambda_B*N_B_mid + lambda_A*N_A_mid)*dt
    N_C[i+1] = N_C[i] + (-lambda_C*N_C_mid + lambda_B*N_B_mid)*dt

plt.figure(figsize=(6,4), dpi=100)
plt.plot(time, N_A, label="Nuclide A", color="red", lw=1, marker='o', ms=3)
plt.plot(time, N_B, label="Nuclide B", color="blue", lw=1, marker='o', ms=3)
plt.plot(time, N_C, label="Nuclide C", color="green", lw=1, marker='o', ms=3)
plt.title("3-Nuclide Decay Chain / "+codename+" Method")
plt.xlabel("Time")
plt.ylabel("N(t)")
plt.xlim(0,t_final)
plt.ylim(0,N_A0+N_B0+N_C0)
plt.grid()
plt.legend()
plt.savefig("10219068_plot.png")
plt.show()
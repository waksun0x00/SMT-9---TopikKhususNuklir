# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:37:30 2023

@author: ASUS
"""

#Python Code: Decay chain 3-Nuclide / Agung Kurniawan (10219068) / Mod Euler Algorithms

import numpy as np
import matplotlib.pyplot as plt

#function to calculate decay chain with euler midpoint (for any-numbers of nuclide)
def decay_chain_euler_midpoint(decay_constants, initial_nuclides, time_step, num_steps):
    num_nuclides = len(decay_constants)
    nuclides = np.zeros((num_steps + 1, num_nuclides))

    # Set the initial nuclides
    nuclides[0] = initial_nuclides

    for i in range(num_steps):
        # Calculate values at the midpoint of the time step
        midpoint_counts = nuclides[i] + 0.5 * time_step * decay_rates(decay_constants, nuclides[i])

        # Calculate values at the next time step
        nuclides[i + 1] = nuclides[i] + time_step * decay_rates(decay_constants, midpoint_counts)
        
    return nuclides

#function to calculate decay rates (for any numbers of nuclides)
def decay_rates(decay_constants, nuclides):
    num_nuclides = len(decay_constants)
    rates = np.zeros(num_nuclides)
    for i in range(num_nuclides):
        for j in range(num_nuclides):
            if j == i-1:
                rate = -decay_constants[i] * nuclides[i] + decay_constants[j]*nuclides[j]
        if i == 0:
            rates[i] = -decay_constants[i] * nuclides[i]
        else:
            rates[i] = rate
    #print(rates)
    return rates

# Calculation Parameters for 3-Nuclides:
Nuclides_name = ['A','B','C']
decay_constants = [0.17, 0.25*0.17, 0.35*0.17]  # List of decay constants for each nuclide
initial_nuclides = [147, 0.10*147, 0.25*147]     # Initial numbers for each nuclide
t_final = 50                    #final time(t) that would be evaluated
num_steps = 50                  # Number of time steps
time = np.linspace(0,t_final,num_steps+1)
time_step = time[1] - time[0]   # Time step (Δt)

#Main Calculations saved at Results Variable
results = decay_chain_euler_midpoint(decay_constants, initial_nuclides, time_step, num_steps)

#Displaying Numerical Calculation for every steps in Console:
print('***** Numerical Calculations Results of Nuclide Decay Chains with Euler Midpoint Algorithms ***** \n')
print('Time(s)   ', end='')
for j in range(len(decay_constants)):
    if j < len(decay_constants) - 1:
        print(f'Nuclide {Nuclides_name[j]:<5}', end='')    
    else:
        print(f'Nuclide {Nuclides_name[j]:<3} \n')

for i in range(num_steps+1):
    print(f'{time[i]:<10.0f}', end='')
    for j in range(len(decay_constants)):
        if j < len(decay_constants) - 1:
            print(f'{results[i][j]:<13.3f}', end='')
        else:
            print(f'{results[i][j]:.3f} \n')

print("*****End of Decay-Chains-Euler mid point Calculations*****")

# Extract some parameters for plotting
codename = "Euler-MidPoint"
#time_plot = np.arange(0,(num_steps+1)*time_step, time_step)

y_max = 0
for i in range(len(decay_constants)):
    y_max += initial_nuclides[i]
    
# Plot results
plt.figure(figsize=(6,4), dpi=100)

for i in range(len(decay_constants)):
    plt.plot(time, results[:,i], label=f'Nuclide {Nuclides_name[i]}', lw=1, marker='o', ms=3)

plt.title("3-Nuclide Decay Chain / "+codename+" Method")
plt.xlabel("Time")
plt.ylabel("N(t)")
plt.xlim(0,t_final)
plt.ylim(0,y_max)
plt.grid()
plt.legend()
plt.savefig("10219068.png")
plt.show()


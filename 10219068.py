# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:47:45 2023

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np

# Partitions
N = 40

#Input Output Array
x = np.zeros(N+1) #x[0] is not used
flux_old = np.zeros(N+1) #y_old[0] is not used
flux_new = np.zeros(N+1) #y_new[0] is not used
source = np.zeros(N+1)

#params
absorb_cs = 0.53 #absorb cross sec
Diff_coef = 0.47 #diff coef
rod_length = 2 #rod_length

# Initial conditions
x[1] = 0 
x[N] = rod_length
dx = (x[N] - x[1]) / (N-1)

#Boundary Conditions
flux_old[1] = 0
flux_old[N] = 0
flux_new[1] = flux_old[1]
flux_new[N] = flux_old[N]
source[1] = 0
source[N] = 0

# Initial guess
flux_guess = 75
for i in range(2, N):
    x[i] = x[i - 1] + dx

flux_old[2:N] = flux_guess
source[2:N] = 25

#Convergence Criteria
err_max = 0.1/100 #Relative % error of numeric and analytic (5% in this case)
itermax = 10000

# Main process
iter = 0
# conv = False
while True:
    conv = 1
    for i in range(2, N):
        flux_new[i] = (flux_old[i + 1] + flux_old[i - 1] + (source[i]/Diff_coef)* dx**2) / (2+(dx**2*absorb_cs))
        # error = np.max(abs((flux_new[2:N] - flux_old[2:N])/flux_new[2:N]))
        error = np.abs((flux_new[i]-flux_old[i])/flux_new[i])
        flux_old[i] = flux_new[i] #Updating Simultaneously after y_new[i] calculations (much faster)
        if error*100 > err_max:
            conv = 0
        
    # Updating Separately (Much Slower Convergence rate)
    # for i in range(2, N):
    #         flux_old[i] = flux_new[i]
    iter += 1
    if conv == 1 or iter > itermax:
        break

print("\nIteration:", iter, "convergence :", conv)
print(f'Max relative error = {100*error:.5f}%')
print("\n#       xi       y_num       y_analytic")
for i in range(1, N+1):
    print(f"{x[i]:10.4f}{flux_new[i]:10.4f}{source[i]:10.4f}")

# Save results to a file
with open("output.txt", "w") as file:
    file.write("\n Iteration: " + str(iter) + "\n")
    file.write("\n#       xi       y_num       y_analytic\n")
    for i in range(1, N + 1):
        file.write(f"{x[i]:10.3f}{flux_new[i]:10.3f}{source[i]:10.3f}\n")

print("\nResult is Saved to output.txt file")

plt.figure(figsize=(6,4), dpi = 100)
plt.plot(x[1:N+1], source[1:N+1], label='Source', color='#FF0000', lw=1, marker='', ms=3)
plt.plot(x[1:N+1], flux_new[1:N+1], label='Flux', color='#0000FF', lw=0, marker='o', ms=3)
plt.title('Finite Difference Method Solutions of Neutron Diff')
plt.xlabel('x (Rod Length)')
plt.ylabel('Flux(x)')
plt.grid()
plt.legend()
plt.savefig("10219068.png")
plt.show()
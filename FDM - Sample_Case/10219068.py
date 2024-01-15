# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:26:55 2023

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np

# Function for the exact solution
def fx(x):
    return 8 * x**3 - 7 * x + 6

# Partitions
N = 20

#Input Output Array
x = np.zeros(N+1) #x[0] is not used
y_old = np.zeros(N+1) #y_old[0] is not used
y_new = np.zeros(N+1) #y_new[0] is not used

# Initial conditions
x[1] = 0 
x[N] = 1
dx = (x[N] - x[1]) / (N-1)

#Boundary Conditions
y_old[1] = 6
y_old[N] = 7
y_new[1] = y_old[1]
y_new[N] = y_old[N]

# Initial guess
y_guess = 0.5 * (y_old[1] + y_old[N])
for i in range(2, N):
    x[i] = x[i - 1] + dx

y_old[2:N] = y_guess

#Convergence Criteria
err_max = 5/100 #Relative % error of numeric and analytic (5% in this case)
itermax = 1000

# Main process

for iteration in range(itermax):
    conv = True
    for i in range(2, N):
        y_new[i] = (y_old[i + 1] + y_old[i - 1] - 48 * dx**2 * x[i]) / 2
        # error = np.max(abs((y_new[2:N] - fx(x[2:N]))/fx(x[2:N])))
        error = np.max(np.abs((y_new[2:N]-y_old[2:N])/y_old[2:N]))
        y_old[i] = y_new[i] #Updating Simultaneously after y_new[i] calculations (much faster)
        if error*100 > err_max:
            conv = False
    print(f'{100*error:.5f}')
    # Updating Separately (Much Slower Convergence rate)
    # for i in range(2, N):
    #         y_old[i] = y_new[i]
    if conv == True:
        break

print("\nIteration:", iter, "convergence :", conv)
print(f'Max relative error = {error:.5f}%, Error Max = {err_max:.5f}')
print("\n#       xi       y_num       y_analytic")
for i in range(1, N+1):
    print(f"{x[i]:10.4f}{y_new[i]:10.4f}{fx(x[i]):10.4f}")

# Save results to a file
with open("output.txt", "w") as file:
    file.write("\n Iteration: " + str(iter) + "\n")
    file.write("\n#       xi       y_num       y_analytic\n")
    for i in range(1, N + 1):
        file.write(f"{x[i]:10.3f}{y_new[i]:10.3f}{fx(x[i]):10.3f}\n")

print("\nResult is Saved to output.txt file")

plt.figure(figsize=(6,4), dpi = 100)
plt.plot(x[1:21], fx(x[1:21]), label='Analytic', color='#FF0000', lw=1, marker='', ms=3)
plt.plot(x[1:21], y_new[1:21], label='Numeric', color='#0000FF', lw=0, marker='o', ms=3)
plt.title('Finite Difference Method Solutions of F"(x) = 48x')
plt.xlabel('x (Spatial Domain)')
plt.ylabel('F(x)')
plt.grid()
plt.legend()
plt.savefig("10219068.png")
plt.show()

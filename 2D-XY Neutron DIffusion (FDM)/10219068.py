import matplotlib.pyplot as plt
import numpy as np

# Partitions
N = 40

#Input Output Array
x = np.zeros((N,N))
flux_old = np.zeros((N,N))
flux_new = np.zeros((N,N))
source = np.zeros((N,N))

#params
absorb_cs = 0.53 #absorb cross sec
Diff_coef = 0.47 #diff coef
plat_dim = 2 #plat dim (meter)

# Initial conditions
dx = plat_dim / (N)
dy = plat_dim / (N)
print(dy)

#Boundary Conditions
# flux_new[0] = flux_old[0]
# flux_new[-1] = flux_old[N-1]
source[:,0] = 0
source[:,-1] = 0
source[0,:] = 0
source[-1,:] = 0

# Initial guess
flux_guess = 75
init_source = 25

source[1:-1,1:-1] = init_source
# source[8:-8,8:-8] = 0
flux_old[1:-1,1:-1] = flux_guess
flux_new[1:-1,1:-1] = (flux_guess+init_source)/2

#Convergence Criteria
iteration = 0
err_max = 1/100 #Relative % error of numeric and analytic (5% in this case)
itermax = 10000
while True:
    conv = 1
    for i in range(1, N-1):
        for j in range(1, N-1):
            flux_new[i,j] = ((flux_old[i+1,j] + flux_old[i-1,j])/(dx**2) + (flux_old[i,j+1] + flux_old[i,j-1])/(dy**2) + (source[i,j]/Diff_coef)) / ((absorb_cs/Diff_coef) + (2/(dx**2)) + (2/(dy**2)))
            error = np.abs((flux_new[i,j]-flux_old[i,j])/flux_new[i,j])
            flux_old[i,j] = flux_new[i,j] #Updating Simultaneously after y_new[i] calculations (much faster)
            if error*100 > err_max:
                conv = 0
        
    iteration += 1
    if conv == 1 or iteration > itermax:
        conv = True
        break

max_flux = np.max(flux_new)
avg_flux = np.mean(flux_new)
peaking_factor = max_flux / avg_flux

print(f"iteration val = {iteration} , convergence = {conv}\n")
print(f'Max relative error = {100*error:.5f}%')
print(f'Peaking Factor = {peaking_factor}')

# print(source)
plt.imshow(flux_new, extent=(0,plat_dim,0,plat_dim), cmap='plasma')
plt.colorbar(label='z=f(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Plot of neutron flux')
plt.savefig('10219068.png')
plt.show()
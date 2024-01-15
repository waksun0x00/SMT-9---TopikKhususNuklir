# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:20:55 2023

@author: ASUS
"""

import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data = np.loadtxt('Data2D.txt')  # Replace 'your_data_file.txt' with the actual filename

#initialize Array or List
rows = 81
columns = 51
x = np.zeros((rows,columns)) #uncomment all of this array or list initialization when using direct ver
y = np.zeros((rows,columns))
z = np.zeros((rows,columns))

# x = []
# y = []
# z = []

# Extract columns (straight/direct version)
# i, j, x, y, z = data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 4]

#Extract columns (iterative ver)
for i in range(0,rows):
    for j in range(0,len(data)):
        if data[j,0] == i+1:
            index_j = int(data[j,1])
            x[i][index_j-1] = data[j,2]
            y[i][index_j-1] = data[j,3]
            z[i][index_j-1] = data[j,4]

#Extract columns (other iterative ver using list)
# for i in range(1,rows+1):
#     x_row = []
#     y_row = []
#     z_row = []
#     for j in range(0,len(data)):
#         if data[j,0] == i:
#             x_row.append(data[j,2])
#             y_row.append(data[j,3])
#             z_row.append(data[j,4])
#     x.append(x_row)
#     y.append(y_row)
#     z.append(z_row)

# x = np.array(x)
# y = np.array(y)
# z = np.array(z)

# Create a 2D plot
plt.scatter(x, y, c=z, cmap='viridis')
plt.colorbar(label='z=f(x,y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Plot of neutron flux')
plt.savefig('10219068.png')
plt.show()

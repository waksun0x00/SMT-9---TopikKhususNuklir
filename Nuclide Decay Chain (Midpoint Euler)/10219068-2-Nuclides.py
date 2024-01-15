#Radioacrive Decay
#N(t) = dN/dt -> N0e(-lambda.t)
#N(n+1) = N(n) - lamba.N(n).delta_t = N(n)(1-lambda.delta.t)
import math
import pandas as pd
import matplotlib.pyplot as plot

def analytic_solution(N0, decay_constant, t):
	N = N0*math.exp(-decay_constant*t)
	return N

def numeric_solution(N_n, decay_constant, delta_t):
	N_i = abs(N_n*(1 - decay_constant*delta_t))
	return N_i

N0 = 100
N_n = 100 
decay_const = 1.32 #(1/s)
t_max = 2 #(s)
delta_t = 0.1 #(s)
t = 0

print('time', 'Numerical', 'analytical')
print(t, '	',N0, '	 ', N0)
with open('rad_decay.txt', 'w') as file:
	file.write('time, numerical, analytical \n')
	file.write('{}, {}, {} \n'.format(t, N_n, N0))
	while t <= t_max:
		t += delta_t
		numeric = numeric_solution(N_n, decay_const, delta_t)
		analytical = analytic_solution(N0, decay_const, t)
		N_n = numeric_solution(N_n, decay_const, delta_t)
		print('{:.1f} {:.3f} {:.3f}'.format(t, numeric, analytical))
		file.write('{:.1f}, {:.3f}, {:.3f} \n'.format(t, numeric, analytical))
		plot.plot(numeric,analytical)
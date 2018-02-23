from matplotlib import pyplot as plt
import numpy as np
import isa
import units as u

N = 200
h = np.linspace(0,70000,N)

T = np.zeros(N)
p = np.zeros(N)
rho = np.zeros(N)

for i in range(N):
	a,b = isa.isa_calc(h[i])
	T[i] = u.centigrade(a.T)
	p[i] = a.p
	rho[i] = a.rho


fig, ax1 = plt.subplots()
ax1.plot(h, p, 'b-')
ax1.set_xlabel('altitude (m)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Pressure (Pa)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(h, T, 'r.')
ax2.set_ylabel('Temperature (C)', color='r')
ax2.tick_params('y', colors='r')
ax2.grid()

fig.tight_layout()
plt.show()

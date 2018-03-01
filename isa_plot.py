from matplotlib import pyplot as plt
import numpy as np
import isa
import units as u

def isa_plot(h0 = 0, h1 = 68000, N=100):
	h = np.linspace(h0,h1,N)

	T = np.zeros(N)
	p = np.zeros(N)
	rho = np.zeros(N)

	for i in range(N):
		a = isa.atm_calc(h[i])
		T[i] = u.temp.k2c(a.T)
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

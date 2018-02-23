from sys import argv
import numpy as np
import isa
import units as u

if len(argv) < 2:
	print(" ")
	print("Please give me the altitude in meters to calculate the results")
	exit()
elif len(argv) > 2:
	print(" ")
	print("More than one parameter received:")
	print("Please give me only one parameter, the altitude in meters")
	exit()

h = int(argv[1])
atm, layer = isa.isa_calc(h)

print("At",h,"m you are in the",isa.layer_name[layer - 1])
print("  Temperature: ", np.round(atm.T,2),"K =",np.round(u.centigrade(atm.T),2),"degree Celsius")
print("  Pressure: ", np.round(atm.p,2), "Pa")
print("  Density: ", np.round(atm.rho,5), "kg/m^3")

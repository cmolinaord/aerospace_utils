# This simple script is used for give the parameters (p, rho, T) of the atmosphere
# at a given altitude, using the International Standard Atmosphere (ISA) model.
#
# In this model, each layer has its own temperature lapse rate.
# The layers will be numbered as follows:
#
# 0 - Tropsosphere
# 1 - Tropopause
# 2 - Stratosphere
# 3 - Stratosphere
# 4 - Stratopause
# 5 - Mesosphere
# 6 - Mesosphere
#
# R = 287 J * Kg^-1 * K^-1
# g = 9.81 m/s^2
#
# a = Temperature lapse rate (degree C/km)
# base_layer_alt = Altitude of the base of the layer indicated by the index (m)
# T0 = Temperature at sea level in ºC
# p0 = pressure at sea level in Pa

import numpy as np
from sys import argv

def kelvin(T_c):
	return T_c + 273.15

def centigrade(T_k):
	return T_k - 273.15

##########################################

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

if h < 0:
	print("Please give an altitude above the sea level (h>0)")
	exit()

print("Altitude: ", h, "m")

R = 287.0
g = 9.81

name = ["Tropsosphere","Tropopause","Stratosphere","Stratosphere","Stratopause","Mesosphere","Mesosphere"]
a = np.array([-6.5,0.0,1.0,2,8,0.0,-2.8,-2.0])
layer_base  = np.array([0,11000,20000,32000,47000,51000,71000])
layer_thick = np.diff(layer_base)

T0 = kelvin(19.0)
p0 = 108900.0
T1 = T0
p1 = p0

layer = 0
#h0 = layer_base[layer]
h1 = h

while h >= layer_base[layer]:
	h1 = np.min([h1,layer_thick[layer]])
	T1 = T0 + 0.001 * a[layer] * h1
	if a[layer] == 0:
		p1 = p0 * np.exp(-1 * g / R / T1 * h1)
	else:
		p1 = p0 * np.power(T1 / T0, -1000 * g / a[layer] / R)

	T0 = T1
	p0 = p1
	h1 = h1 - layer_thick[layer]
	layer += 1

# Density calculated with Gas equation
rho = p1 / R / T1

print("You are in the",name[layer - 1])
print("  Temperature: ", np.round(T1,2),"K =",np.round(centigrade(T1),2),"degree Celsius")
print("  Pressure: ", np.round(p1,2), "Pa")
print("  Density: ", np.round(rho,5), "kg/m^3")

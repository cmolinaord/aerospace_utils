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
import units as u

##########################################
# Objects

class gas_state(object):
	__slots__ = ["T","p","rho"]
	def __init__(self, T, p, rho):
		self.T = T
		self.p = p
		self.rho = rho

##########################################
# Variables

layer_name = ["Tropsosphere","Tropopause","Stratosphere","Stratosphere","Stratopause","Mesosphere","Mesosphere"]

##########################################
# Functions

def isa_calc(h):
	if h < 0:
		print("Please give an altitude above the sea level (h>0)")
		exit()

	R = 287.0
	g = 9.81

	a = np.array([-6.5,0.0,1.0,2,8,0.0,-2.8,-2.0])
	layer_base  = np.array([0,11000,20000,32000,47000,51000,71000])
	layer_thick = np.diff(layer_base)

	T0 = u.kelvin(19.0)
	p0 = 108900.0

	atm = gas_state
	atm.T = T0
	atm.p = p0

	layer = 0
	#h0 = layer_base[layer]
	h1 = h

	while h >= layer_base[layer]:
		h1 = np.min([h1,layer_thick[layer]])
		T1 = atm.T + 0.001 * a[layer] * h1
		if a[layer] == 0:
			p1 = atm.p * np.exp(-1 * g / R / atm.T * h1)
		else:
			p1 = atm.p * np.power(T1 / T0, -1000 * g / a[layer] / R)

		atm.T = T1
		atm.p = p1
		h1 = h1 - layer_thick[layer]
		layer += 1

	# Density calculated with Gas equation
	atm.rho = atm.p / R / atm.T

	return atm, layer

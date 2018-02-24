import const

class temp:
	# Temperature units conversion
	def c2k(T):
		return T + const.T_K

	def k2c(T):
		return T - const.T_K

class dist:
	ft = 0.3048

	def ft2m(d):
		return d * dist.ft

	def m2ft(d):
		return d / dist.ft

class pressure:
	bar = 1e5
	atm = 101325

	def bar2Pa(p):
		return p * pressure.bar

	def Pa2bar(p):
		return p / pressure.bar

	def atm2Pa(p):
		return p * pressure.atm

	def Pa2atm(p):
		return p / pressure.atm

class density:
	def kgm3Togm3(rho):
		return 1000 * rho

	def gm3Tokgm3(rho):
		return 0.001 * rho

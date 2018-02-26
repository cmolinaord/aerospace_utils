import const

class time:
	# Time units conversion
	m = 60
	h = 3600
	day = 86400

	def min2sec(t):
		return t * 60

	def hour2min(t):
		return t * 60

	def day2sec(t):
		return t * time.day



class temp:
	# Temperature units conversion
	def c2k(T):
		return T + const.T_K

	def k2c(T):
		return T - const.T_K

class dist:
	ft = 0.3048 # m
	nmi = 1852 # Nautical mile to meters

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

class velocity:
	def ms2kmh(vel):
		return vel * 3.6

	def kmh2ms(vel):
		return vel / 3.6

	def kn2ms(vel):
		return vel * dist.nmi / time.h

	def ms2kn(vel):
		return vel * time.h / dist.nmi

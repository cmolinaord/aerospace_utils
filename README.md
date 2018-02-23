# Aerospace_utils

Aerospace_utils aims to be a collection of useful functions to calculated
aeronautical and aerospace related parameters and results.

I don't pretend to create a very complex library with infinite functionallity, but
I'll try to add everything I would need for ease calculations needed in my carrer.

# Tools
## ISA

ISA (International Standard Atmosphere) is an ideal model for Earth Atmosphere,
which don't take into account non-idealities of gases, wheater conditions or
other gases as water vapor or suspended particles or dust.

### isa.py
isa.py implements a series of functions like isa_calc, which calculates the
thermodynamical variables of the air at a given altitude.

Usage: `gas_state, layer = isa_calc(altitude)`
where:

- gas_state = object containing the thermodynamical values at given altitude:
  - gas_state.T = Temperature in kelvin
  - gas_state.p = pressure in Pa
  - gas_state.rho = density in Kg/m<sup>3</sup>
- layer = the number of the layer at given altitude
- altitude: in meters above sea level

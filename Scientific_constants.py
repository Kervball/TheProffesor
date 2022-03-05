import math


pico = p = 10**-12
n = nano = 10**-9
u = micro = 10**-6

Kilo = K = 10**3
Mega = M = 10**6
Giga = G = 10**9

k_const = Boltz_const = 1.38*10**-23 #joules per Kelvin
k_ev_const = boltz_ev_const = 8.62*10**-5

u_0 = 4*math.pi*10**-7

class boltz_const:
    joules = Boltz_const
    ev = boltz_ev_const

k = planks = boltz_const()

planks_const = h_const = 6.63*10**-34 #joules a second
planks_ev_const = h_ev_const = 4.14*10**-15

class planks_class:
    joules = h_const
    ev = h_ev_const

planks = h = planks_class()

q = 1.60217*10**-19 #coulombs

c_const = lightspeed_const = 3*10**8 #meters
c_cm_const = lightspeed_cm_const = 2.998*10**10

class lightspeedclass:
    meters = lightspeed_const
    cm = lightspeed_cm_const

c = lightspeedclass()
lightspeed = lightspeedclass()
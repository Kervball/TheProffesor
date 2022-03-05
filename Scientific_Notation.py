'''This file contains basic notation for all engineering topics'''
import math
#bring in constants
from Scientific_constants import *
#bring in greek symbols
from Greek_symbols import *
#bring in unit classes
from Sci_units import *

#measurments with all the conversions and units

class Temperature():
    def __init__(self, K = None, C = None, F = None):
        if F:
            C = (F-32)*5/9
        elif C:
            F = (C*5/9)+32
            K = C +237
            
        K = C +237    
        self.K = K
        self.C = C
        self.F = F
        

#conversions

    #trig
def radians_to_degrees(radians):
    return math.degrees(radians)

def degrees_to_radians(degrees):
    return math.radians(degrees)

def Sin_degrees(degrees):
    radians_in = degrees_to_radians(degrees)
    radians_out = math.sin(radians_in)
    return radians_to_degrees(radians_out)

    #db
def Feild_to_DB(feild):
    return math.log10(feild)*20

def Energy_to_DB(feild):
    return math.log10(feild)*10

def dB_to_feild(dB):
    return 10**(dB/20)

    #eV
def Joules_to_eV(joules):
    return joules*6.242*10**18

def ev_to_Joules(eV):
    return eV*1.602*10**-19


def Scale(value, symbol = None):
    #expects values in base unit
    return_string = ""
    if value < nano:
        return_string = "{:.4f} pico".format(value /pico)
    elif value < micro:
        return_string =  "{:.4f} nano".format(value /nano)
    elif value < 10**-3:
        return_string=  "{:.4f} μ".format(value /micro)
    elif value < 1:
        return_string = "{:.4f} m".format(value /10**-3)
    elif value > G:
        return_string=  "{:.4f} G".format(value /G)
    elif value > M:
        return_string=  "{:.4f} K".format(value /M)
    elif value > K:
        return_string =  "{:.4f} K".format(value /K)
    else:
        return_string =  "{:.4f}".format(value)

    if symbol == 'OMEGA':
        return_string += omega_sym

    if symbol == 'AMPS':
        return_string += "A"

    return return_string

#controls system library from princton
#https://web.math.princeton.edu/~cwrowley/python-control/index.html

import math
import matplotlib.pyplot as plt
from Scientific_Notation import *


#getting underdamped values
def Getomega_d(W_n, damping):
    return W_n*math.sqrt(1-damping**2)

def GetSettleTime(W_n, Damping):
    return 4/(W_n*Damping)

def GetOvershoot(damping):
    return math.exp(-math.pi*damping/math.sqrt(1-damping**2))

def GetDamping(overshoot):
    overshoot /= 100
    numerator = -1*math.log(overshoot)
    denominator = math.sqrt(math.pi**2+ math.log(overshoot)**2)
    return numerator/denominator


def GetOmega_n(damping, settle_time):
    return settle_time/(2*damping)


def GetK_Val(real_root, poles, imagniary_root):
    #add the pole and the real values
    elements = []
    real_root = -1*real_root
    for pole in poles:
        elements.append(real_root+pole)
    K = 1
    #now take magnitude of each pole and root
    for number in elements:
        K *= math.sqrt(number**2+imagniary_root**2)
    return K
    
def Get_desired_root(damping, T_S):
    W_n = 4/(T_S *damping)
    W_d = Getomega_d(W_n, damping)
    angle = Get_dampingline_angle(damping)
    return "Desired root: {} +/- {:.2f}j\nwhich should intesect along {:.2f} degrees\nW_n : {:.3f}".format(T_S,W_d, angle, W_n)

def Get_dampingline_angle(damping):
    return radians_to_degrees(math.acos(damping))

def FindNew_Wc(phase_degrees, phase_arr, freq ):
    upper_limit = phase_degrees*1.009
    lower_limit = phase_degrees*.992
    print("Desired Value: ", phase_degrees)
    count = 0
    for i in phase_arr:
        count += 1
        degrees = radians_to_degrees(i)
        if (degrees <= lower_limit) and (degrees >= upper_limit):
            print(count, " |W:", freq[count] ," Phase angle:" , radians_to_degrees(i),)

def GetPoleAngles(roots, W_d, real):
    P_angles = 0
    for root in roots:
        if root < real:
            distance_to_root = real-root
            angle = radians_to_degrees(math.atan(W_d/(distance_to_root)))
            P_angles += 180-angle
        else:
            distance_to_root = root-real 
            angle = radians_to_degrees(math.atan(W_d/(distance_to_root)))
            P_angles += angle
    return P_angles

def GetZeroRe(angle, W_d):
    angle = math.radians(angle)
    return W_d/math.tan(angle)


def GetPhaseMargin_damp(damping):
    #section 11.2 in zyBook
    numerator = 2*damping
    squareone = math.sqrt(1+4*damping**4)
    denominator = math.sqrt(-2*damping**2+ squareone)
    return math.atan(numerator/denominator)

######## printing functions
def printOmegaD():
    omega_n = int(input("W_n: "))
    damping = int(input("Damping: "))
    return "W_d: {:.2f}".format(Getomega_d(omega_n, damping))

def PrintDamping():
    overshoot = int(input("Overshoot: "))
    print("Damping: {:.2f}".format(GetDamping(overshoot)))

######graphing

def nyquist_graph(real, ima, title):
    # plotting the points
    plt.plot(real, ima)
    # giving a title to my graph
    plt.title(title)
    # function to show the plot
    # naming the x axis
    plt.xlabel("real")
    # naming the y axis
    plt.ylabel("imaginary")
    plt.show()
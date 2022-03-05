from Greek_symbols import *
import math

class Vector:
    def __init__(self):
        print("Not finished")


class Power:
    def __init__(self, Watts = None, VAR = None, pf = None, VA = None ):
        self.angle = None #this will be changed but we want to check along the way
        

        if Watts:
            Watts = float(Watts)
        
        if VAR:
            VAR = float(VAR)
        
        self.VAR = VAR
        self.pf = pf
        self.Watts = Watts

        if pf:
            self.angle = math.acos(pf)
        elif Watts and VAR:
            self.angle = math.tan(VAR/Watts)
            self.pf = math.cos(self.angle)


        if VA:
            self.VA = VA
        elif Watts and VAR:
            self.VA = (self.Watts**2+self.VAR**2)**(1/2)
        elif Watts and self.angle:
            self.VA = self.Watts*math.cos(self.angle)

    def __str__(self):
        return_statment = ""
        if self.Watts:
            return_statment += "{:.4} Watts".format(self.Watts)
        
        if self.VAR:
            return_statment += "{:.4} VAR".format(self.VAR)
        
        if self.pf:
            return_statment += "{:.4} pf".format(self.pf)


        return return_statment

            



class Resistance:

    def __init__(self, Ohm = None, mOhm = None, KOhm = None):
        self.baseUnit = omega_sym
        
        if not Ohm and not mOhm and not KOhm:
            raise "must have unit"
            
        if Ohm:
            self.base = Ohm
        elif mOhm:
            self.base = mOhm/1000
        elif KOhm:
            self.base = KOhm*1000
        
        self.Ohm = self.base
        self.mOhm = self.base*1000
        self.KOhm = self.base/1000
        
        

    def __mul__(self, I):
        if type(I) == Current:
            return Voltage(V = self.base*I.base)
        else:
            return Resistance(Ohm = self.base * I)

    def __truediv__(self, divisor):
        if type(divisor) == Resistance:
            return self.base / divisor.base
        else:
            return Resistance(Ohm = self.base / divisor)

    def __str__(self):
        value = ""
        if self.base > 1000:
            value = "{:.4f} K{}".format(self.KOhm, omega_sym)
        elif self.base < 1:
            value = "{:.4f} m{}".format(self.mOhm, omega_sym)
        else:
            value = "{:.4f} {}".format(self.base, self.baseUnit)
        return value

class Current:
    
    def __init__(self, A = None, mA = None, KA = None):
        self.baseUnit = 'A'
        if A:
            self.base = A
        elif mA:
            self.base = mA/1000
        elif KA:
            self.base = KV*1000
        
        self.A = self.base
        self.mA = self.base*1000
        self.KA = self.base/1000
    
    def __str__(self):
        value = ""
        if self.base > 1000:
            value = "{:.4f} {}".format(self.KA, "KA")
        elif self.base < 1:
            value = "{:.4f} {}".format(self.mA, "mA")
        else:
            value = "{:.4f} {}".format(self.base, self.baseUnit)
        return value
    
    def __mul__(self, R):
        if type(R) == Resistance:
            return Voltage(V = self.base*R.base)
        else:
            return Current(A = self.base*R)

class Voltage:
    def __init__(self, RMS = False, mV = None, V = None, KV = None, eV = None):
        self.baseUnit = 'V'
        if eV:
            self.base = 1.602176*10**-19
        elif V:
            self.base = V
        elif mV:
            self.base = mV/1000
        elif KV:
            self.base = KV*1000
        
        self.mV = self.base*1000
        self.KV = self.base/1000
        self.V = self.base
    
    def __str__(self):
        value = ""
        if self.base > 1000:
            value = "{:.4f} {}".format(self.KV, "KV")
        elif self.base < 1:
            value = "{:.4f} {}".format(self.mV, "mV")
        else:
            value = "{:.4f} {}".format(self.base, self.baseUnit)
        return value

    def __add__(self, v_2):
        return Voltage(V = (v_2.base + self.base))
    
    def __truediv__(self, divisor):
        if type(divisor) == Resistance:
            return Current(A = self.base / divisor.base)
        elif type(divisor) == Current:
            return Resistance(Ohm=self.base / divisor.base)

class Volume:
    def __init__(self,mm3 = None, cm3 = None, feet3 = None, ounce = None, gallon = None):
        self.baseUnit = 'mm3'
        if mm3:
            self.base = mm3
        elif cm3:
            self.base = cm3*10**3
        elif feet3:
            self.base = feet3*2.8317*10**7
        elif ounce:
            self.base = ounce*29573.5296
        elif gallon:
            self.base = gallon*3.7854*10**6
        
        self.mm3 = self.base
        self.cm3 = self.base/10**3
        self.feet3 = self.base/2.8317*10**7
        self.ounce = self.base/29573.5296
        self.gallon = self.base/3.7854*10**6
    
    def __str__(self):
        value = "{:.4f} {}".format(self.base, self.baseUnit)
        return value

    def __add__(self, v_2):
        return Volume(mm3 = (v_2.base + self.base))

    def __sub__(self, v_2):
        return Volume(mm3 = (v_2.base - self.base))

class Area:
    def __init__(self, mm2 = None, cm2 = None, inches2 = None, feet2 = None, 
    meters2 = None):
        self.baseUnit = 'mm2'
        if mm2:
            self.base = mm2
        elif cm2:
            self.base = cm2*100
        elif inches2:
            self.base = inches2*654.16
        elif feet2:
            self.base = feet2*92903.04
        elif meters2:
            self.base = meters2*10*6
        self.meters2 =  self.base/10**6
        self.feet2 = self.base/92903.04
        self.inches2 = self.base/654.16
        self.cm2 = self.base/100
        self.mm2 = self.base
        
    def __str__(self):
        value = "{:.2f} {}".format(self.base, self.baseUnit)
        return value
    
    def __add__(self, l_2):
        return Area(mm2 = (l_2.base + self.base))
    
    def __sub__(self, l_2):
        return Area(mm2 = (l_2.base - self.base))
    
    def __mul__(self, len_2):
        if type(len_2) == Length:
            return Volume(mm3= (self.mm2 * len_2.mm))
        else:
            return Area(mm2 = self.base*len_2)

class Length:

    def __init__(self, mm = None, cm = None, inches = None, feet = None, 
    meters= None,  yards = None, miles = None, km = None):
        self.baseUnit = 'mm'
        if mm:
            self.base = mm
        elif cm:
            self.base = cm*10
        elif inches:
            self.base = inches*25.4
        elif feet:
            self.base = feet*304.8
        elif meters:
            self.base = meters*1000
        elif yards:
            self.base = yards*914.4
        elif miles:
            self.base = miles*1609344
        elif km:
            self.base = km*10**6

        self.mm = self.base
        self.cm = self.base/10
        self.inches = self.base/25.4
        self.feet = self.base/304.8
        self.meters = self.base/10**3
        self.yards = self.base/914.4
        self.miles = self.base/1609344
    
    def __add__(self, l_2):
        return Length(mm= (l_2.base + self.base))
    
    def __sub__(self, l_2):
        return Length(mm= (l_2.base - self.base))

    def __str__(self):
        value = "{:.2f} mm".format(self.base)
        return value

    def __mul__(self, l_2):
        if type(l_2) == Length:
            mm_squared = l_2.mm *self.mm
            return Area(mm2 = mm_squared)
        else:
            return Length(mm = self.base * l_2)
    
    def __pow__(self, times):
        return Area(mm2 = self.base**times)
from group_6 import *
from math import pi
from const import E0
k = 1 / (4 * pi * E0)
        
# find electric field, voltage between objects
# Ecyl = -Q/(E0*2*pi*r*h)
# Esph = Q/(E0*4*pi*r^2)
# Vsph = 0

class asymmetric_cap(capacitor):                    #class capacitor
    def __init__(self, h, sep, r_cyl, r_sph, ref):  #has attributes incl height, separation, radii
        Q = 10                                      #arbitrary definition
        self.h = float (h)                          
        self.r_cyl = float (r_cyl)
        self.r_sph = float (r_sph)
        self.sep = float(sep)
        self.ref = ref

        dx = 1.0e-3                                      # integration to find deltav
        phi = 0.0
        for i in xrange(int ((sep-(r_cyl+r_sph))/dx)):   # considering sep as s+radii
            x = (dx * i) + r_sph
            Ecyl = Q /(E0 * 2 * pi * x * h)              # as defined above
            Esph = Q /(E0 * 4 * pi * x **2)
            phi += (Ecyl + Esph) * dx 

        self.capacitance = Q / (phi)                     # capacitance = Q/V         
        self.q = 0.0
        print phi


class super_cap(capacitor):                              #part 2
    def __init__(self, cap1, cap2, parallel, ref):
        self.cap1 = 
        self.cap2 =
        self.parallel = 
        self.ref = ref

 def charge(self, voltage):
        self.q = self.capacitance * voltage             # charge class
        self.ref[self] = self.q

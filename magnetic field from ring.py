import numpy as np
from math import sin, cos, pi
from const import mu0
dtheta = 1e-4                                       

I = I #uh not really sure what to put here          # Ring Properties I in amp, R in m
R = a

def B(x,y,z):                                           # For the moment, we only vary z
    P = np.array((x, y, z))
    B = np.array((0.0, 0.0, 0.0))
    for i in xrange(int(2 * pi / dtheta)):
            theta = i * dtheta
            pos = R * np.array((cos(theta),         # Location of differential current
                                sin(theta),
                                0.0))
            r = P - pos
            r_mag = np.linalg.norm(r)
            dl = R * dtheta * np.array((-sin(theta),# Differential wire vector, a positive current flows CCW from the top
                                        cos(theta),
                                        0.0))
            dB = (mu0 * I * np.cross(dl, r) /       # Biot-Savart Law
                  (4.0 * pi * r_mag**3))
            B = B + dB
    return B

def analyticalB(x,y,z):
    B = ((mu0 * I * R**2) /
           (2.0 * (z**2 + R**2)**(3 / 2.0)))
    return np.array((B_x, B_y, B_z))

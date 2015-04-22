aimport numpy as np
from math import sin, cos, pi
from const import mu0
dtheta = 1e-4
mu_0 = 4 * pi * 1e-7

I = current #uh not really sure what to put here except an integer   # Ring Properties I in amp, R in m
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

N = number of turns
l = length of solenoid

B_sol_inside = (mu_0 * I * N)/l                  #I know we can calculate B_inside from Ampere's and B_outside from Biot-Savart, not sure how to combine here
return B_sol

# Have you considered using the one-ring function you wrote up above to add several rings'
# magnetic fields together? This would work both inside and outside the solenoid.
def B_sol_outside(0.0,0.0,z):                                           # For the moment, we only vary z
    P = np.array((0.0, 0.0, z))
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

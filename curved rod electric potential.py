#normal imports

import time
import numpy as np
#from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp, sin, cos, e
from const import E0

k = 1.0 / (4 * pi * E0)

# defining charge density and phi

def lamda(theta) :
    return 10e-6 / (1 + e**-5 * (theta - pi/2))

def phi (point):
         # need to fix interval of integration to -pi/2 to pi/2?  
    C = pi
    dth = 1.0e-3

    phi = 0.0
    for i in xrange(int(C / dth)):
             dq = lamda(i * dth) * dth / 2
             pos = (np.array([cos(i*dth), 0.5 + sin(i*dth), 0]))   
             r = np.linalg.norm(point - pos)     
             phi += k * dq / r
    return phi

#graphing - still don't understand the denominators under j/__ for y,z components

start = time.time()
path = range(50)
V = []
for j in path:
    V.append(phi(np.array([0.02, j / 20.0, j / 30.0])))

#plot(path, V)
#print start - time.time()
#show ()

#calculating theoretical expression of electric potential
           
def lamda(theta) :
    return 10e-6 / (1 + e**-5 * (theta - pi/2))
           
def phi_th(P):
    pos = (np.array([cos(theta), 0.5 + sin(theta), 0]))
    r = np.linalg.norm(point - pos)

    phi_th=-k / (10e7 * r) * (log(ee(5 * pi)))
    return phi_th

#calculating err

V= []
V1 = []
err = []

err = (abs(phi - phi_th)/(phi_th))




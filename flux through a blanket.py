from math import sqrt, pi, cos, sin                               # Gather constants and functions
from const import E0
k = 1.0 / (4 * pi * E0)

def E(q, P):
    r = (P[0] - q[0], P[1] - q[1], P[2] - q[2])
    mag = sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
    field = []
    field.append(k * (r[0] / mag) * (q[3] / (mag**2)))  # Calculate x, y, and z components
    field.append(k * (r[1] / mag) * (q[3] / (mag**2)))
    field.append(k * (r[2] / mag) * (q[3] / (mag**2)))
    return field

dx = 10e-3
dy = 10e-3

for i in xrange(int(2/ (dx))):
    for j in xrange(int(2/ (dy))):
        P = [i-1, j-1, 1]
q = [0,0,0,10e-6]
print E(q, P)[0]
flux = 0
flux = flux +E(q, P) [2]*dx*dy
print i,j,flux


sigma = 10e-3
force = flux * (sigma)
print force

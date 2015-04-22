from math import pi
import numpy as np
dt = 1e-3
numPoints = int(1e4)

m = 10e-22                              #Particle characteristics
q = 1.6e-19
lamda = 1e-15
I = 1e-4
mu_0 = 8.85e-12

startPos = np.array((1.0, 1.0, 1.0))         #Initial conditions
startVel = np.array((10.0, 5.0, 5.0))

# It's a Gauss' Law problem. You draw a cylinder around the wire,
# then calculate the electric field from the flux. Or you could do an integral
# analytically from -pi/2 to pi/2 and calculate the electric field that way.
# That's why we gave you the wire's charge density.
##E = wait how do I define an electric field here?
##Fe = q * E

with open('trajectory.txt', 'w', 0) as text:     #Opening text file
    pos = startPos
    vel = startVel
    for iteration in xrange(numPoints):
        t = dt * iteration
        B = (mu_0 * I)/(2 * pi * pos)          #Defining magnetic field
        Fb = np.cross(q * vel, B)
        F = Fb                              #This would be F = Fb + Fe if I knew what Fe was
        a = F / m
        vel = vel + a * dt                 
        pos = pos + vel * dt
        pVec = pos.tolist()                 # Organizing file
        vVec = vel.tolist()
        aVec = a.tolist()
        text.write(str((pVec, vVec, aVec)) + '\n') 

from math import sqrt, pi
from const import E0
k = 1.0 / (4 * pi * E0)

def bob(charge, location):
    q = charge
    l = location
    distance = [None, None, None]
    distance = [q[0]-l[0], q[1]-l[1], q[2]-l[2]]
    d = distance
#defined function to include charge and location 
    E_0 = [None, None, None]
    mag=sqrt((d[0]**2)+d[1]**2+d[2]**2)

    E_0[0] = k * (q[3]/(mag**2)) * (d[0] / mag)
    E_0[1] = k * (q[3]/(mag**2)) * (d[1] / mag)
    E_0[2] = k * (q[3]/(mag**2)) * (d[2] / mag)

    E_tot = [None, None, None]
    E_tot = [E_0[0] , E_0[1] , E_0[2]]
#found electric field components
    print 'E =', E_tot, 'N/C'

bob((2, 7, -2, -1), (6, 3, -4000000000))

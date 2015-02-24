from math import sqrt, pi
from const import E0
from visual import *
k = 1.0 / (4 * pi * E0)

def bob(charge, location):
        q = charge
        l = location
        distance = [None, None, None]
        distance = [q[0]-l[0], q[1]-l[1], q[2]-l[2]]
        d = distance
        print distance

        #defined function bob to contain charge, location

        E_0 = [None, None, None]
        mag=sqrt((d[0]**2)+d[1]**2+d[2]**2)
        print mag

        E_0[0] = k * (q[3]/(mag**2)) * (d[0] / mag)
        E_0[1] = k * (q[3]/(mag**2)) * (d[1] / mag)
        E_0[2] = k * (q[3]/(mag**2)) * (d[2] / mag)

        E_tot = [None, None, None]
        E_tot = [E_0[0] , E_0[1] , E_0[2]]

        return E_tot

        #calculated E_tot

a = bob((0, 1, 0, 1), (0, 0, 0))
b = bob((0, -1, 0, -1), (0, 0, 0))

E_ab = [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

a_1 = arrow (pos = vector(0,0,0), axis=vector ((1.0/10000000)*E_ab[0], 0, 0), color = color.red)
a_2 = arrow (pos = vector(0,0,0), axis=vector (0, (1.0/10000000)*E_ab[1], 0), color = color.red)
a_3 = arrow (pos = vector(0,0,0), axis=vector (0, 0, (1.0/10000000)*E_ab[2]), color = color.red)

print E_ab

#defined arrows to be components of E field, note to grader: the first arrows are subject to evil computer magic and refuse to coexist with the peaceful green arrows, the green arrows work perfectly fine in their pacifist world, I promise

c = bob((0, 1, 0, 1), (1, 3, 5))
d = bob((0, -1, 0, -1), (1, 3, 5))

E_cd = [c[0]+d[0], c[1]+d[1], c[2]+d[2]]

b_1 = arrow (pos = vector(1,3,5), axis=vector ((1.0/10000000)*E_cd[0], 0, 0), color = color.green)
b_2 = arrow (pos = vector(1,3,5), axis=vector (0, (1.0/10000000)*E_cd[1], 0), color = color.green)
b_3 = arrow (pos = vector(1,3,5), axis=vector (0, 0, (1.0/10000000)*E_cd[2]), color = color.green)

print E_cd

sleep(0.01)






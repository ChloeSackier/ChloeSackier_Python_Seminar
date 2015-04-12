from __future__ import division
from visual import *
import numpy as np
from math import pi

print("""
Use mouse to do stuff
""")

path = 'trajectory.txt'

scene.title = "Path of positively charged particle in magnetic field"
scene.forward = vector(0, -.5, -1)

pos = []
vel = []
a = []

with open(path, 'r', 0) as trajectory:
    line = trajectory.readline()

    while line:
        raw_numbers = line.split(', ')
        data = []

        for val in raw_numbers:
            data.append(float(val.strip('])([\n')))

        pos.append(data[0:3])
        vel.append(data[3:6])
        a.append(data[6:9])
        line = trajectory.readline()

path = curve( color = color.red, radius = 0.1)

n = 0
while n < len(pos) - 1:
        rate(100)
        path.append( pos = vector(pos[n]) )
        n = n + 1

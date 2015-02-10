from visual import *

Sue=sphere (pos = vector (-1,0,0), radius = 0.25, color = color.green)
Bob=sphere (pos = vector (1,1,0), radius = 0.25, color = color.green)
Chloe=sphere (pos = vector (1,-1,0), radius = 0.25, color = color.green)

arrow (pos = Sue.pos, axis = Chloe.pos-Sue.pos, color = color.red)
arrow (pos = Chloe.pos, axis = Bob.pos-Chloe.pos, color = color.red)
arrow (pos = Bob.pos, axis = Sue.pos-Bob.pos, color = color.red)

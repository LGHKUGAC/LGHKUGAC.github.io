#paste your code here:
from turtle import *
speed(0)
r = 20
rh = 300/r
x = 212
y = 175
z = 55
nc = 10    
h = 0
colormode(255)
def CC(x, y, z, rh):
    penup()
    goto(-200, -150) 
    pendown()
    
    for i in range(r):  
        fillcolor(int(x), int(y), int(z))
        pencolor(int(x), int(y), int(z))
        begin_fill()
        for _ in range(2):
            forward(400)  
            left(90)
            forward(rh) 
            left(90)
        end_fill()
        penup()
        goto(-200, -150 + (i + 1) * rh)
        pendown()
        x = min(255, x + nc)
        y = min(255, y + nc)
        z = min(255, z + nc)
CC(x, y, z, rh)
for i in range(16):
    for j in range(18):
        c = pick_random_color_()
        color(c)
        h += 0.005
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
        circle(40, 24)
CC(212,175,55, 300/20)


#paste your code here:
from turtle import *

petals = random.randint(2,20)
fc = pick_random_color_()
pc  = pick_random_color_()
length_rays = random.randint(30,200)
speed(-100)

pencolor(pc)
fillcolor(fc)
bgcolor("black")
r,g,b=200,0,0

goto(-2, -55)
for i in range(petals):
        begin_fill()
        circle(95-i,45)
        left(45)
        end_fill()
        circle(95-i,45)
        left(9)
        

goto(0, 0)
for i in range(15):
  forward(length_rays)
  backward(length_rays)
  left(30)


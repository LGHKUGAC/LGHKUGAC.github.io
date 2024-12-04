#paste your code here:
from turtle import *
speed(0)
bgcolor('forestgreen')
r=6
y=6
X = 5
color = pick_random_color_()

for i in range(10):
  pensize(X)
  pencolor(color)
  pendown()
  circle(r)
  penup()
  goto(0, -y)
  r = r + 10
  y = y + 10
goto(0, 5)
pensize(4)
pencolour('skyblue')
pendown()

angle = 360 / 6

for i in range(6):
  forward(70)
  backward(70)
  left(angle)




 


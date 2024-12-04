#paste your code here:
from turtle import *
right(180)
speed(8)
bgcolor('navy')
pencolor('black')
pensize(2)
def draw_logo(x, y, r, g, b, length):
  j = 0
  penup()
  goto(x, y)
  pendown()
  for i in range(3):
    if j <= 0:
      c = 0
    elif r > 20:
      r = r-20
    elif g > 20:
      g = g-20
    elif b > 20:
      b = b-20
    else:
      c = 0
    fillcolor(r, g, b)
    begin_fill()
    backward(length)
    forward(3*length)
    right(120)
    forward(5*length)
    left(120)
    forward(length)
    left(60)
    forward(6*length)
    left(120)
    forward(5*length)
    left(120)
    forward(length)
    end_fill()
    right(180)
    backward(length)
    j = (j+1)
  return
draw_logo(0, 0, 110, 193, 160, 20)





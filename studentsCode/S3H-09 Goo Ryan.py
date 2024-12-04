from turtle import *
speed(10)
red = 120
green = 240
blue = 100
bgcolor(red,green,blue)
red = 18
green = 137
blue = 255
pencolor(red,green,blue)
pensize(6)
for i in range(10):
  red = 255
  green = 204
  blue = 255
  fillcolor(red,green,blue)
  begin_fill()
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  left(360/10)
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  left(72)
  forward(60)
  end_fill()

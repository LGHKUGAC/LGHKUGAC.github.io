from turtle import *
bgcolor('black')
fillcolor('skyblue')
pencolor('royalblue')
pensize(10)
speed(10)

side = 6
angle = 360/side
radius = 30
begin_fill()

for i in range(side):
  circle(radius)
  left(60)
end_fill()

pensize(5)

for i in range(side):
  forward(50)
  backward(50)
  left(60)
  
pencolor('yellow')

for i in range(4):
  forward(5)
  penup()
  forward(5)
  pendown()
  forward(5)
  penup()
  backward(15)
  left(90)

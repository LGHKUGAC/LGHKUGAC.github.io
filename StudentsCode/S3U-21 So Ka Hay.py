#paste your code here:
from turtle import *
speed(10)
bgcolor('black')
left(90)
penup()
forward(60)
left(90)
backward(60)
pendown()
pencolor('green')
fillcolor('green')
begin_fill()
for loop in range(4):
  forward(120)
  left(90)
end_fill()
penup()
goto(0, 0)
pendown()
pencolor('red')
fillcolor('hotpink')
angle = 360/10
begin_fill()
for loop in range(10):
  circle(30)
  left(angle)
end_fill()


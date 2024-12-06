#paste your code here:
from turtle import *
bgcolor('black')
fillcolor('royalblue')
pensize(7)
pencolor('blue')
speed(0)
sides = 7
angle = 360 / sides


begin_fill()

for i in range(sides):
  forward(45)
  left(angle)
  
end_fill()



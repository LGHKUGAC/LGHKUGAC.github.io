#paste your code here:
from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

# Write your code below!
speed(0)
pensize(5)
bgcolor('black')
fillcolor('hotpink')
begin_fill()
points = 7
angle = 360/ points
for i in range(points):
  draw_petal('purple')
  left(angle)
end_fill()


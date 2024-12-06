#paste your code here:

from turtle import *
def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

# Write your code below!
bgcolor('black')
fillcolor('white')
pencolor('wheat')
pensize(5)
speed(0)

radius = 50
angles = 360 / 7
begin_fill()

for i in range(8):
  circle(radius)
  left(60)
  
for i in range(10):
  circle(radius)
  left(60)

fillcolor('tan')
pencolor('saddlebrown')


end_fill()


#paste your code here:

from turtle import *
speed(150)
bgcolor('black')

def draw_petal(colour):
  pencolor(colour)

  for i in range(4):
    forward(60)
    left(90)

# Write your code below!
pensize(5)
fillcolor('skyblue')
length = 20
angle = 360/length
begin_fill()
for k in range(length):
  draw_petal('purple')
  left(angle)
end_fill()

pencolor('pink')
pensize(4)
slices = 10

angle = 360 / slices

for i in range(slices):
  forward(80)
  backward(80)

  left(angle)


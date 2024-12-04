from turtle import *


def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)
    
  
pensize(5)
fillcolor('orange')
length = 9
angle = 360/length
begin_fill()
for k in range(length):
  draw_petal(pick_random_color_())
  left(angle)
end_fill()


pensize(4)
slices = 9

angle = 360 / slices

for i in range(slices):
  # Draw a cut
  forward(110)
  backward(110)
  
  left(angle)
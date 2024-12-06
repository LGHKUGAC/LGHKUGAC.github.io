#paste your code here:
from turtle import *
speed(0)
fillcolor('pink')
begin_fill()
def draw_logo():
  for i in range(8):
    right(45)
    circle(20)
  
    forward(30)
    backward(30)
    left(45)
    forward(30)
    backward(30)
    left(45)

draw_logo()
left(45)
forward(80)
draw_logo()

draw_logo()
right(120)
forward(80)
draw_logo()

draw_logo()
right(60)
forward(80)
draw_logo()

draw_logo()
right(60)
forward(80)
draw_logo()

draw_logo()
right(65)
forward(80)
draw_logo()
  
end_fill()


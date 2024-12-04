from turtle import *

radius = 15
def draw_circle(colour):
  pencolor(colour)
  for i in range(15):
    circle(radius)
    left(90)
    fillcolor('white')

radius = 15
speed(0)
pensize(5)
bgcolor('lightblue')

begin_fill()
draw_circle('pink')
fillcolor('lightblue')
#for i in range(5):
 # circle(radius)
  #left(angle)


end_fill() 


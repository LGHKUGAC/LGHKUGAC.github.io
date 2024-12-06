from turtle import *
bgcolor('black')
radius = 50
def draw_circle(colour):
  pencolor(colour)
  for i in range(15):
    circle(radius)
    left(90)
    fillcolor('lightblue')

radius = 50
speed(0)
pensize(5)
bgcolor('black')

begin_fill()
draw_circle('pink')
fillcolor('lightblue')
#for i in range(5):
 # circle(radius)
  #left(angle)


end_fill() 


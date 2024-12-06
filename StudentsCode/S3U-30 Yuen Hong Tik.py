#paste your code here:

from turtle import *

def hexagon(size):
  angle = 360/6
  for i in range(6):
    forward(size)
    left(angle)
    forward(size)


   
side_length = 40
length=40
pensize(5)
pencolor('orange')
fillcolor('pink')
bgcolor('black')
length = 30 
colour = 'red' 
begin_fill()
for i in range(3):
  hexagon(side_length)
  right(360/3)
 
end_fill()


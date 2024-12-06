#paste your code here:
from turtle import *

speed(0)

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(50)
    left(45)

pensize(5)
bgcolor('black')
fillcolor('cornflowerblue')

petals = 60             
angles = 360 / 60 
begin_fill ()
          
for loop in range(60):
      draw_petal('plum’')
      left(angles)
      goto(0, 0)
end_fill()
   
             
for loop in range(2):
  for loop in range(2):
        draw_petal('plum')
        left(angles)
        goto(0, 0)


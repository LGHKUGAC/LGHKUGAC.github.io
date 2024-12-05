#paste your code here
from turtle import *

def draw_logo(colour):
  pencolor(colour)
  for i in range(8):
    forward(90)
    left(120)
 # Adjust the speed
speed(0) #Set speed to maximum for quick drawing
pensize(3)
bgcolor('black')
fillcolor('skyblue')
vine =18 
staff = 360 / vine
begin_fill()
for i in range(vine):
  draw_logo('purple')
  left(staff)
  
  
end_fill()

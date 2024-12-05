#paste your code here:
from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    circle(petal)
def draw_snowflake(colour):
  pencolor(colour)
  for i in range(4):
    forward(120)
    left(90)
def draw_square(colour):
  pencolor(colour)
  for i in range(4):
    forward(100)
    left(90)
speed(0)

bgcolor('black')
pensize(3)
pencolor('white')
fillcolor('white')
petal = 20
snowflake = 70
square = 35
angle =(360/petal)
angle_2 =(360/snowflake)
begin_fill()

for i in range(petal): 
  left(angle)
  draw_petal('white')
 
end_fill()

begin_fill()
for i in range(snowflake): 
    fillcolor('darkblue')
    left(angle_2)
    draw_snowflake('white')
end_fill()
for i in range(square): 
  left(angle)
  draw_square('black')
    
  



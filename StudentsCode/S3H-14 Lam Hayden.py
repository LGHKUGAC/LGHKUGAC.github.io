#paste your code here:

from turtle import *

speed(15)
pencolor('red')
pensize(5)

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90) 
    
degrees = 360/24

for i in range(24): 
  for s in range(4):
    forward(50)
    right(90)
  right(degrees)
  bgcolor('navyblue')
  
  right(90)
  forward(100)



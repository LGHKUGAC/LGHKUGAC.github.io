#paste your code here:
from turtle import *

from turtle import *
speed("fastest")

def background(): #background color
  penup()
  setpos(-200, 150)
  pendown()
  for x in range(255):
    pencolor(121, 170, 247)
    setpos(200, 150-x)
    setpos(-200, 150-x)
background()

penup()
goto(0, 0)
pendown()
pencolor(97, 7, 133)
num_shapes = 90 #customisation for logo


degrees = 360/num_shapes 


for i in range(num_shapes): 
  for s in range(4): 
    forward(50)
    right(90)
  right(degrees) #repeated squares creates a cirle with different patterns such as stars
  
penup() #forming the letter "c"
pensize(10)
right(90)
forward(100)
left(90)
pendown()
forward(15)
right(45)
forward(15)
penup()
right(180)
forward(15)
left(45)
pendown()
forward(30)
left(90)
forward(38)
left(90)
forward(40)


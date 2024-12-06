#paste your code here:
from turtle import *
colour = 0
pencolor(colour,colour,colour)
speed(10)
angle = 360/3
penup()
goto(0, 0)
pendown()
fillcolor('white')
bgcolor(0, 0, 0)

def draw_logo(length):
  pensize(5)
  penup()
  for i in range(12):
    begin_fill()
    for i in range(3):
      forward(50)
      left(90)
    forward(50)
    left(angle)
    end_fill()
  pendown()  
  for i in range(12):
    pencolor(i*2,i*2,i*255/12)
    penup()
    forward(20)
    pendown()
    forward(20)
    backward(20)
    penup()
    backward(20)
    pendown()
    left(30)
  pencolor('black')
  pensize(20)
  circle(1)
  penup()
  goto(-75, -75)
  pendown()
  pensize(1)
  for i in range(4):
    for i in range(200):
      import random
      value = (random.randint(0,255))
      value_2 = (random.randint(0,255))
      value_3 = (random.randint(0,255))
      pencolor(value, value_2, value_3)
      forward(0.75)
    left(90)
     
draw_logo(50)



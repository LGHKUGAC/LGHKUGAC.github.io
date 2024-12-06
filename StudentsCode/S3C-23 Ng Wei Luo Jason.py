#paste your code here:
from turtle import *
import random
speed(0)
d = 1
e = 1
bgcolor('black') 
for i in range(50):
  red = 5
  green = 5
  blue = 225
  pencolor(red + i, green + i, blue) 
  penup()
  goto(0,0)
  right(90)
  forward(d)
  left(90)
  pendown()
  circle(e)
  d = d+1
  e = e+1
for i in range(100):
  red = 5
  green = 5
  blue = 225
  pencolor(red + i, green + i, blue) 
  penup()
  goto(250,100)
  right(90)
  forward(d)
  left(90)
  pendown()
  circle(e)
  d = d+1
  e = e+1
for i in range(100):
  red = 100
  green = 100
  blue = 225
  pencolor(red + i, green + i, blue) 
  penup()
  goto(-250,0)
  right(90)
  forward(d)
  left(90)
  pendown()
  circle(e)
  d = d+1
  e = e+1
for i in range(100):
  pencolor('cyan')
  pensize(5)
  penup()
  goto(0,0)
  pendown()
  right(45)
  forward(100 + i)



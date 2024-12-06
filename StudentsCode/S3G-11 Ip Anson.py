#paste your code here:
from turtle import *

bgcolor('black')
fillcolor('orange')
pensize(7)



speed(0)


for i in range(13):
  begin_fill()
  color('skyblue')
  forward(75)
  left(25)
  forward(75)
  left(25)
  forward(75)
  left(25)
  backward(78)
  right(25)
  backward(78)
  right(25)
  left(90)
  penup()
  forward(50)
  pendown()
  backward(50)
  right(25)
  penup()
  color('white')
  forward(90)
  left(75)
  pendown()
  circle(25)
  end_fill()


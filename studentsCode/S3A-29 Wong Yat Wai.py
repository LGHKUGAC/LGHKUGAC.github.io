#paste your code here:
from turtle import *
import random
speed(10)
bgcolor('black')
x = 360/7
pensize(10)
pencolor('white')
for i in range(7):
  def circleshit(color):
    if i == 0:
      return 'lightcoral'
    elif i == 1:
      return 'darkorange'
    elif i == 2:
      return 'gold'
    elif i == 3:
      return 'yellowgreen'
    elif i == 4:
      return 'limegreen'
    elif i == 5:
      return 'powderblue'
    elif i == 6:
      return 'mediumpurple'
  fillcolor(circleshit(color))
  begin_fill()
  circle(50)
  end_fill()
  left(x)

pensize(4)
for i in range(7):
  def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
  fillcolor(color())
  begin_fill()
  forward(40)
  right(120)
  forward(40)
  right(120)
  forward(40)
  right(120)
  end_fill()
  left(x)
penup()
right(90)
forward(40)
left(90)
pendown()
pensize(7)
circle(40)


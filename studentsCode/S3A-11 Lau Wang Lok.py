#paste your code here:
from turtle import *
def drawlogo():
  speed(0)
  r = 255
  g = 255
  b = 0
  x = -232
  y = -232
  for a in range(255):
    penup()
    goto(x , y)
    pendown()
    pencolor(r , g , b)
    circle(50)
    x = x + 1.7
    y = y + 1.7
    r = r - 1
    g = g - 1
    b = b + 1
    






a = random.choice(['red', 'green', 'blue'])
bgcolor(a)

drawlogo()


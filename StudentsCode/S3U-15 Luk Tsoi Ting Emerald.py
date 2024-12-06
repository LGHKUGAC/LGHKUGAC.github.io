#paste your code here:
from turtle import *
speed(0)
length = 50
bgcolor('black')
r = 30
def draw_logo():
  color('red')
  global r
  for i in range(16):
   circle(r)
   r = r + 20
   left(30)
draw_logo()
end_fill()


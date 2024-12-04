from turtle import *
bgcolor('black')
pensize(5)
speed(0)
penup()
goto(-95, 0)
pendown()
colormode(255)
for i in range(152):
  color(0, 255 - i, 0 + i)
  forward(i * 5)
  circle(200, 52)
  right(170)
def draw_leaf():
  begin_fill()
  circle(20, 90)
  left(90)
  circle(20, 90)
  left(90)
  end_fill()

def draw_logo():
  speed(0)
  penup()
  radius = 0
  goto(0, radius)
  pendown()
  color('lightcyan')
  for i in range(12):
    draw_leaf()
    penup()
    goto(0, radius)
    pendown()
    right(30)
draw_logo()

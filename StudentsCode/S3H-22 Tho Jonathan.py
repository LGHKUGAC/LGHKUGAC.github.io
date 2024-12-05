#paste your code here:

from turtle import *
def draw_arrow(x, y, value):
  penup()
  goto(x, y)
  pendown()
  forward(50)
  for i in range(10):
    forward(10)
    right(20)
  left(20)
  forward(100)
  for i in range(10):
    forward(10)
    right(20)
  left(20)
  forward(50)
fillcolor('#355FF9')
begin_fill()
speed(0)
bgcolor(0, 0, 0)
pencolor('white')
pensize(7)
draw_arrow(0, 30, 0)
penup()
left(90)
draw_arrow(-28.5, 0, 0)
right(90)
penup()
end_fill()


goto(0, -28.5)
fillcolor('red')
begin_fill()
pendown()
circle(30)
penup()
end_fill()
goto(0, 0)



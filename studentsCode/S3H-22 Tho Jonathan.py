from turtle import *
def draw_arrow(x, y, value):
  penup()
  pencolor(value, value + 25, value + 25)
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

begin_fill()
speed(5)
bgcolor(100, 20, 30)
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
fillcolor('#FF6464')
begin_fill()
pendown()
circle(30)
penup()
end_fill()
goto(0, 0)



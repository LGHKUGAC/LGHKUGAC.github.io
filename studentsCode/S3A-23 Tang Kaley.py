#paste your code here: 

from turtle import *
speed(0)
bgcolor('black')
pensize(2)
red = 204
green = 255
blue = 229
pencolor(red, green, blue)
red = 0
green = 180
blue = 180
fillcolor(red, green, blue)
begin_fill()
for _ in range(12):
    circle(50)
    left(30)
end_fill()
pensize(5)
pencolor('lightblue')
fillcolor('white')
begin_fill()
for k in range(10):
  for i in range(4):
    forward(60)
    left(90)
  left(36)
end_fill()
pensize(4)
pencolor('purple')
fillcolor('pink')
begin_fill()
backward(60)
for u in range(10):
  for h in range(4):
    forward(100)
    left(144)
  left(36) 
end_fill()
def draw_star(size):
    for _ in range(5):
        forward(size)
        left(144)
penup()
setpos(-120, -120)
pendown()
pensize(6)
red= 255
green= 102
blue= 178
pencolor(red, green, blue)
for _ in range(4):
    forward(240)
    left(90)
def draw_star(size):
    for _ in range(5):
        forward(size)
        left(144)


hideturtle()
done()


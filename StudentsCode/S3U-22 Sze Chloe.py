#paste your code here:
from turtle import *
bgcolor('skyblue')
speed(10)
pencolor('black')
pensize(10)
pensize(5)
goto(5,2.5)
forward(30)
left(90)
forward(5)
left(90)
forward(30)
goto(10,-2.5)
forward(25)
left(90)
forward(5)
left(90)
forward(50)
goto(15, -7.5)
forward(25)
left(90)
forward(5)
left(90)
forward(50)
goto(20,-10)
forward(50)
left(90)
forward(5)
left(90)
forward(70)
left (90)
forward(5)
left(90)
forward(70)
penup()
right(90)
forward(50)
right(90)
forward(70)
left(90)
forward(70)
pendown()
def draw_petal(colour):
  pencolor(colour)
for i in range(4):
    forward(60)
    left(90)
bgcolor('skyblue')
fillcolor('azure')
pensize(5)
angle = 75
begin_fill()
for loop in range(5):
  draw_petal('cornsilk')
  left(angle)
for loop in range(5):
  draw_petal('lightsteelblue')
  left(angle)
for loop in range(5):
  draw_petal('honeydew')
  left(angle)
for loop in range(5):
  draw_petal('powderblue')
  left(angle)
for loop in range(5):
  draw_petal('lavender')
  left(angle)
  left(angle)
end_fill()
pencolor('black')
left(80)
forward(100)


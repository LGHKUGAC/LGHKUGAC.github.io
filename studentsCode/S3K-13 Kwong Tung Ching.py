#paste your code here:
from turtle import *
from turtle import *
bgcolor("black")
speed(0)
p = 3
pencolor("white")
pensize(p)
fillcolor("lightblue")
begin_fill()
circle(45)
a= 360/45
for i in range(45):
  right(a)
  penup()
  forward(45)
  pendown()
  circle(45)
  right(20)
  forward(30)
  right(90)
  forward(20)
  
penup()
forward(140)
right(30)
pendown()
forward(100)
right(130)
forward(100)
penup()
forward(100)
left(90)
pendown()
forward(100)
right(130)
penup()
right(90)
forward(100)
pendown()
forward(100)
right(130)
end_fill()



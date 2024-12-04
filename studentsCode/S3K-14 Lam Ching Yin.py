#paste your code here:

from turtle import *
pencolor(pick_random_color_())
fillcolor(pick_random_color_())
speed(10)
pensize(5)
bgcolor("black")

penup()
left(180)
forward(30)

forward(40)
pendown()

begin_fill()
for i in range(1):
  circle(30)
end_fill()

begin_fill()
right(180)
forward(30)
right(90)
forward(30)
end_fill()

penup()
forward(30)
left(90)
forward(45)
left(90)
forward(5)
right(90)
right(20)
pendown()

pencolor(pick_random_color_())
circle(15,45)
left(45)
circle(15,45)
circle(180,45)
circle(15,45)
left(45)
circle(15,45)
circle(180,45)


penup()
goto(0,0)
setheading(0)

begin_fill()
for i in range(1):
  circle(30)
end_fill()

begin_fill()
right(180)
forward(30)
right(90)
forward(30)
end_fill()



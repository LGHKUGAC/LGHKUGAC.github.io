#paste your code here:
from turtle import *
speed(20)
bgcolor('black')
#first square
pencolor('firebrick')
fillcolor('firebrick')
penup()
goto(-15,-15)
pendown()
begin_fill()
for i in range(3):
  forward(30)
  left(90)
forward(30)
end_fill()
penup()
forward(5+3)
left(90)
forward(3)
pendown()
#second square
pencolor('orangered')
fillcolor('orangered')
begin_fill()
for i in range(3):
  forward(24)
  right(90)
forward(24)
end_fill()
penup()
left(180)
forward(24+5+3+6)
left(90)
forward(3)
pendown()
#third square
pencolor('darkorange')
fillcolor('darkorange')
begin_fill()
for i in range(3):
  forward(18)
  right(90)
forward(18)
end_fill()
penup()
right(90)
forward(18+5+6+9)
right(90)
forward(3)
left(90)
pendown()
#fourth square
pencolor('orange')
fillcolor('orange')
begin_fill()
for i in range(3):
  forward(12)
  right(90)
forward(12)
end_fill()
penup()
right(90)
forward(12+5+9+12)
right(90)
forward(3)
left(90)
pendown()
#fifth square
pencolor('gold')
fillcolor('gold')
begin_fill()
for i in range(3):
  forward(6)
  right(90)
forward(6)
end_fill()
penup()
forward(5+12+9)
left(90)
forward(3)
right(90)
pendown()
#sixth square
pencolor('orange')
fillcolor('orange')
begin_fill()
for i in range(3):
  forward(12)
  right(90)
forward(12)
end_fill()
penup()
forward(5+9+6)
left(90)
forward(3)
right(90)
pendown()
#seventh square
pencolor('darkorange')
fillcolor('darkorange')
begin_fill()
for i in range(3):
  forward(18)
  right(90)
forward(18)
end_fill()
penup()
left(180)
forward(18+6+5+3)
right(90)
forward(3)
left(90)
pendown()
#eighth square
pencolor('orangered')
fillcolor('orangered')
begin_fill()
for i in range(3):
  forward(24)
  left(90)
forward(24)
end_fill()
penup()
forward(5+3+6)
left(90)
forward(3)
right(90)
pendown()
#nineth square
pencolor('darkorange')
fillcolor('darkorange')
begin_fill()
for i in range(3):
  forward(18)
  left(90)
forward(18)
end_fill()
penup()
#go back to the first square and draw the 'E'
goto(-5,7)
pendown()
pencolor('white')
pensize(4)
forward(14)
left(90)
forward(12)
backward(12)
left(90)
forward(7)
right(90)
forward(10)
backward(10)
left(90)
forward(7)
right(90)
forward(12)
backward(12)



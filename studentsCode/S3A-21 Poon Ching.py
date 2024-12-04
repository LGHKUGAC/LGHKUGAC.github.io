#paste your code here:
from turtle import *
speed(10)
Length = random.randint(30,70)
bgcolor('darkblue')
fillcolor('springgreen')
pencolor('orangered')
pensize(3) 
degees = 30/Length
begin_fill()
for i in range(14):
  left(30)
  backward(Length)
  forward(Length)
  
forward(Length)
left(90.5)
circle(Length)
end_fill()
begin_fill()
end_fill()
pensize(2)
pencolor('red')

penup()
backward(15)
pendown()
penup()
goto(0,0)
pendown()
fillcolor('cyan')
right(90)
side = 50
angle = 144
begin_fill()
for i in range(5):
  forward(Length)
  forward(90)
  left(angle)
  forward(90)
  left(angle)
  forward(90)
  left(angle)
  forward(90)
  left(angle)
  forward(90)
  right(36)
  forward(Length)
  left(30)

  
end_fill()
 
end_fill()



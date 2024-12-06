#paste your code here:
from turtle import*
speed(0)
def draw_petal(colour):
  pencolor(colour)
  circle(50)
pensize(5)
def triangle(colour):
  pencolor(colour)
  for i in range(3):
    right(120)
    forward(20)
def diamond(colour):
  pencolor(colour)
  for i in range(2):
     forward(30)
     right(60)
     forward(30)
     right(120)
bgcolor('grey')
fillcolor('royalblue')
begin_fill()

for i in range(10):
  draw_petal('hotpink')
  left(360/10)

penup()
goto(0,0)
pendown()
for i in range(4):
  left(30)
  diamond('yellow')
  right(120)
penup()
goto(10,5)
pendown()
for i in range(1):
  triangle('red')
end_fill()


#paste your code here:

from turtle import *
speed(0)
length=40

def draw_shape(colour):
  pencolor(colour)
  for i in range(n):
    forward(length)
    left(angle)
    
pensize(5)
bgcolor('midnightblue')
fillcolor('white')
  
n = 5
angle = 180-(((n-2)*180)/n)
angle2 = 360/n
  
begin_fill()

for i in range(n):
  draw_shape('royalblue')
  left(angle2)
  
end_fill()

penup()
goto(-50,-70)
pendown()
forward(100)

penup()
goto(-40,-80)
pendown()
forward(80)

penup()
goto(-30,-90)
pendown()
forward(60)




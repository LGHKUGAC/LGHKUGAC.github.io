#paste your code here:

from turtle import *
def draw_icon(colour):
  pencolor(colour)
  for i in range(1):
   circle(17)
  
def draw_icon2(colour):
  pencolor(colour)
  for i in range(1):
   circle(14)
  
from turtle import *
speed(10)
bgcolor('black')
pencolor('lightpink')
pensize(2)
fillcolor('lightpink')

penup()
forward(50)
pendown()

for i in range (10):
  draw_icon2('white')
  left(360/10)

penup()
right(180)
forward(100)
pendown()

for i in range (10):
  draw_icon2('white')
  left(360/10)

penup()
right(180)
forward(50)
pensize(5)
pendown()
  
begin_fill()
for i in range (5):
 left(360/5)
 draw_icon('pink')
end_fill()

penup()
left(45)
forward(50)
pendown()



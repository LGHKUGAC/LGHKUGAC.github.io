#paste your code here:

from turtle import *

bgcolor('black')

speed(0)

def draw_logo(value):
  
  for i in range(100):
    pencolor(value, value, value)
    forward(i * 2)
    right(121)
    value = value - 2.5
        
draw_logo(255)
penup()
goto(0, 0)
pendown()
draw_logo(254)
penup()
goto(0, 0)
pendown()
draw_logo(253)
penup()
goto(0, 0)
pendown()
draw_logo(252)
penup()
goto(0, 0)
pendown()
draw_logo(251)
penup()
goto(0, 0)
pendown()
draw_logo(250)



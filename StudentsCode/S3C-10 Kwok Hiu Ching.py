#paste your code here:

from turtle import *

square_side = ((40**2*2)**0.5)
square_fillcolor = "cornflowerblue"
circle_fillcolor = "aquamarine"
speed(10)

def draw_square(color):
  penup()
  goto(0, -40)
  pendown()
  fillcolor(color)
  begin_fill()
  for i in range(4):
    forward(square_side)
    left(90)
  end_fill()
  
def draw_circle(color):
  penup()
  goto(0,0)
  pendown()
  fillcolor(color)
  begin_fill()
  for i in range(4):
    circle(37)
    left(90)
  end_fill()
  
def bg_circle(red, green, blue):  
  for i in range(6):
    fillcolor(red, green, blue)
    begin_fill()
    circle(50)
    end_fill()
    left(360/12)
    green = green - 20
    blue = blue - 20
  for i in range(5):
    fillcolor(red, green, blue)
    begin_fill()
    circle(50)
    end_fill()
    left(360/12)
    green = green + 20
    blue = blue + 20
  for i in range(2):
    fillcolor(red, green, blue)
    pendown()
    begin_fill()
    circle(50, 210)
    penup()
    goto(0,0)
    left(180)
    pendown()
    circle(50, 150)
    end_fill()
    penup()
    left(360/12)
    green = green + 20
    blue = blue + 20
    goto(0,0)
    left(180)
  right(360/12)
  

bgcolor("darkblue")
bg_circle(255,250,205)
draw_circle("aquamarine")
left(45)
draw_square("cornflowerblue")
draw_circle("pink")



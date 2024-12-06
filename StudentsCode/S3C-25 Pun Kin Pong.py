#paste your code here:
from turtle import *
hideturtle()
speed(0)
def triangle():#function for making a triangle on the right
  begin_fill()
  forward(30)
  left(120)
  forward(30)
  left(120)
  forward(30)
  end_fill()
def leftTriangle():#function for making a triangle on the left
  left(180)
  triangle()
  backward(30)
  left(60)
def sideTriangle(): #
  left(120)
  forward(30)
  left(60)
  triangle()
def sidePartLogo():
  leftTriangle()
  triangle()
  leftTriangle()
  triangle()
  leftTriangle()
  triangle()
  leftTriangle()
def bottomTriangles():
  left(60)
  triangle()
  sideTriangle()
  sideTriangle()
def background():
  penup()
  setpos(-200, 150)
  pendown()
  a=0
  for x in range(190):
    pencolor(190-x, 190-x, 190-x)
    for x in range(2):
      setpos(200, 150-a)
      setpos(-200, 150-a)
      a+=1
def logo():
  penup()
  pencolor(255,255,255)
  goto(-30,80)
  left(30)
  pendown()
  sidePartLogo()
  right(120)
  triangle()
  bottomTriangles()
  bottomTriangles()
  left(60)
  triangle()
  sideTriangle()
  left(60)
  right(240)
  forward(30)
  right(120)
  triangle()
  right(180)
  triangle()
background()
speed(11)
logo()


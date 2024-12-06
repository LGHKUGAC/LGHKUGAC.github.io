#paste your code here:
from turtle import *
bgcolor('black')
speed(0)#speed of drawing
r=5#setting radius
color("red")#setting color for the flower 1
for i in range(40):#making flower 1
  circle(r,50)
  r=r+1
right(90)
pendown()
color("hotpink")
circle(r,270)
right(180)
circle(r,270)
right(180)
circle(r,270)
right(180)
circle(r,270)
penup()
color("green")#making the leaf for flower 1
forward(100)
pendown()
right(10)
circle(130,60)
right(250)
circle(90,60)
penup()
forward(40)
left(160)
pendown()
forward(120)
penup()
backward(20)
right(45)
pendown()
l=15
forward(l)
penup()
backward(l)
left(90)
pendown()
forward(l)
penup()
backward(l)
right(45)
backward(20)
pendown()
for i in range(3):#making flower 2
  right(45)
  forward(l+5)
  penup()
  backward(l+5)
  left(90)
  forward(l+5)
  pendown()
  backward(l+5)
  right(45)
  backward(20)
penup()
right(130)
forward(160)
pendown()
color(160,130,230)
for i in range(24):#making flower 3
  right(130)
  forward(l)
  l=l+5
right(140)
forward(100)
penup()
right(90)
forward(200)
pendown()
p=20
color("yellow")
for i in range(24):#making flower 4
  right(130)
  forward(p)
  p=p+1
penup()
left(45)
forward(60)
pendown()
color(255,128,0)
for i in range(24):
  right(130)
  forward(p)
  p=p+1



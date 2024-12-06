#paste your code here:
from turtle import *
speed(0)
def tri():
  for i in range(1,7):
    circle(i*5+25,180)
  
def square():
  circle(13,180)
  forward(40)
  circle(13,180)
  forward(40)

pensize(5)
penup()
left(90)
forward(200)
right(90)
pendown()
pencolor(255, 255, 255)
forward(200)
backward(400)
for i in range (1, 80):
  pencolor(0, 15+i*3, 15+i*3)
  right(90)
  forward(5)
  left(90)
  forward(400)
  backward(400)
  
speed(10)
penup()
goto(-20,-20)
pendown()

pencolor('#0d0385')
fillcolor('#9dfcfc')
begin_fill()


for i in range(5):
  left(360/5)
  tri()

end_fill()


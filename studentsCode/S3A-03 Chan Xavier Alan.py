from turtle import *
bgcolor('black')
speed(0)
a = 0
c = 0
y = 45
z = 135
hideturtle()
pensize(3)
pencolor(255, 127, 0)
fillcolor(255, 255, 0)
def sf():
  forward(15)
def lf():
  forward(120)
def st():
  left(y)
def lt():
  left(z)
begin_fill()
for i in range (4):
  for i in range(8):
    st()
    for i in range(2):
      sf()
      st()
      lf()
      lt()
  left(11.25)
end_fill()
right(45)
penup()
forward(150)
left(90)
pendown()
pencolor(0, 255, 127)
pensize(5)
for i in range(360):
  forward(2.61799387799)
  left(1)
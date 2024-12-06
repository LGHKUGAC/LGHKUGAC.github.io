#paste your code here:

from turtle import *

speed(10)
bgcolor('dark')
pensize(5)
pencolor('#B8BC86')
penup()
right(90)
forward(60)
left(90)
pendown()

for i in range(4):
  fillcolor('#d38fc4')
  begin_fill()
  forward(60)
  left(90)
  forward(60)
  end_fill()
  
penup()
right(90)
forward(30)
left(90)
pendown()


for i in range(4):
  fillcolor('#E799A3')
  begin_fill()
  forward(90)
  left(90)
  forward(90)
  end_fill()

penup()
right(90)
forward(30)
left(90)
pendown()

for i in range(4):
  fillcolor('#98AFC7')
  begin_fill()
  forward(120)
  left(90)
  forward(120)
  end_fill()
  
penup()
goto(0,0)

pendown()
pencolor('#fdb813')
dot(20)
pencolor('#fcd065')
dot(10)
pencolor('#ffe8b0')
dot(5)



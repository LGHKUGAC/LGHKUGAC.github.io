#paste your code here:
from turtle import *
speed(0)

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

pensize(5)
bgcolor('black')
fillcolor('white')
angle = 360 / 100
begin_fill()
for i in range (100):
  draw_petal('darkgray')
  left(angle)
pencolor('white')
left(90)
forward(60)
right(150)
forward(120)
right(120)
forward(120)
right(120)
forward(120)
right(150)
forward(60)

def draw_petal2(colour):
  pencolor(colour)
  for i in range(4):
    forward(20)
    left(90)

pensize(2)
fillcolor('lightgray')
angle = 360 / 15
begin_fill()
for i in range (15):
  draw_petal2('black')
  left(angle)
end_fill()


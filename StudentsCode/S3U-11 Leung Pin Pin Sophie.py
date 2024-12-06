#paste your code here:
from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(15):
    forward(50)
    left(90)
speed(0)
pensize(14)
bgcolor('black')
petals = 10
angle = 500/petals
for i in range(petals):
  draw_petal('mediumblue')
  left(angle)
def draw_petal(colour):
  pencolor(colour)
  for i in range(15):
    forward(45)
    left(1000)
speed(0)
pensize(7)
bgcolor('black')
petals = 10
angle = 120/petals
for i in range(petals):
  draw_petal('orange')
  left(angle)





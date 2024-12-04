#paste your code here:

from turtle import *

def draw_petal(colour):
  pencolor(colour)
  for i in range(5):
    forward(60)
    left(72)
    
import random
def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
random_color = random_color_generator()

speed(0)
bgcolor('navy')
pensize(5)
r = 10
for i in range (11):
  pencolor(random_color)
  pendown()
  circle(r)
  penup()
  right(90)
  forward(10)
  left(90)
  r = r + 10

left(90)
forward(120 )
fillcolor('plum')
pendown()    
begin_fill()
for i in range(5):
  draw_petal = pencolor('gold')
  for i in range(5):
    forward(60)
    left(72)
  right(72)
end_fill()

right(50)
fillcolor('cornflowerblue')
begin_fill()
for i in range(5):
  draw_petal = pencolor('yellow')
  for i in range(3):
    forward(70)
    left(120)
  left(72)
end_fill()

right(50)
fillcolor('mistyrose')
begin_fill()
for i in range(5):
  draw_petal = pencolor('gold')
  for i in range(3):
    forward(50)
    left(120)
  left(72)
end_fill()

for i in range(10):
  forward(20)
  draw_petal = pencolor('orange')
  circle(3)
  backward(20)
  left(36)


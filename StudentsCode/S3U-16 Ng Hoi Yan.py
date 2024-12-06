#paste your code here:
from turtle import*
bgcolor('black')
r = 55
y = 10 
fillcolor('lightpink')
begin_fill()
def star():
  forward(y)
  right(108)
  forward(y)
  left(36)
  forward(y)
  right(108)
  forward(y)
  left(36)
  forward(y)
  right(108)
  forward(y)
  left(36)
  forward(y)
  right(108)
  forward(y)
  left(36)
  forward(y)
  right(108)
  forward(y)
  left(36)
  
 
  
for i in range(6):
  speed(0)
  pensize(4)
  pencolor('orange')
  star()
  penup()
  left(r)
  forward(50)
  pendown()
penup()
pencolor('white')
right(90)
forward(30)
left(110)
pendown()
circle(85)
left(90)
penup()
forward(30)
pendown()
pencolor('yellow')
pensize(30)
circle(10)
end_fill()
penup()
forward(55)
pensize(5)

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(80)
    left(90)
fillcolor('hotpink')
petals = 8
angle = 360 / petals
begin_fill()
for _ in range(petals):
  draw = draw_petal('purple')
  left(angle)
end_fill()

penup()
forward(132452)

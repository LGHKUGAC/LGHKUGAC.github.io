from turtle import *
pencolor('skyblue')
pensize(5)
bgcolor('royalblue')
fillcolor('lightblue')
begin_fill()
c = 7
r = 20
angle = 360/c
u = right(90)
b = 40
def draw_petal(blue):
  pencolor(blue)
  for i in range(4):
    forward(60)
    left(90)
for i in range (c):
  circle(r)
  left(angle)
  forward(90)
  backward(90)
  left(angle)
  circle(b)
  left(angle)
end_fill()
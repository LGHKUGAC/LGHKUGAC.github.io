#paste your code here:
from turtle import *
speed(0)
def draw_petal(skyblue):
  pencolor(skyblue)
  for i in range(4):
    forward(60)
    left(90)

bgcolor('black')
fillcolor('skyblue')
begin_fill()
pensize(5)
pencolour('skyblue')
petals = 5
angle = 360 / petals

for i in range (petals):
  petal = draw_petal('grey')
  left(angle)
end_fill()

def draw_petal(color):
    pencolor(color)
    for i in range(4):
        forward(60)
        left(90)
def draw_center_circle():
    penup()
    goto(0, -30)
    pendown()
    fillcolor('cornflowerblue')
    begin_fill()
    circle(30)
    end_fill()
    penup()
    goto(0, 0)


bgcolor('grey')
fillcolor('blue')
begin_fill()
pensize(5)
pencolor('royalblue')
petals = random.randint(3,7)
angle = 360 / petals

for i in range(petals):
    draw_petal('black')
    left(angle)

end_fill()

draw_center_circle() 


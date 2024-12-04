#paste your code here:
from turtle import *


speed(0)

def draw_petal():
    outline_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    pencolor(outline_color)
    fillcolor(fill_color)
    
    begin_fill()
    for i in range(4):
        forward(60)
        left(90)
    end_fill()


pensize(3)
bgcolor('black')

a = random.randint(5,7)
length = random.randint(20,50)
b = random.randint(5,7)
x = 360 / a

for i in range(a):
    draw_petal()
    left(x)

def firework(colour1, colour2, x, y):
    pensize(4)
    penup()
    goto(x, y)
    pendown()
    for i in range(20):

        colour1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colour2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pencolor(colour1)
        forward(length)
        backward(length)
        right(9)
        pencolor(colour2)
        forward(length / 2)
        backward(length / 2)
        right(9)


if __name__ == '__main__':
    firework('cyan', 'paleturquoise', 0, 0)

r = 100
y = -105

for i in range(b):
    r = r + 5
    penup()
    goto(0, y)
    pendown()
    y = y - 5
    circle(r)
    pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



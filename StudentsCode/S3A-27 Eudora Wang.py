from turtle import *

speed(0)
pensize(4)

def draw_petal(colour,l):
    pencolor(colour)
    for i in range(4):
        forward(l)
        left(90)
bgcolor('black') 
a = 20
x = 360 / a
for i in range(a):
    draw_petal('orange',100)
    left(x)
    
color('blue')
fillcolor('red')
begin_fill()
a = 20
x = 360 / a
for i in range(a):
    draw_petal('grey',60)
    left(x)
end_fill()


penup()
goto(-100, 0)
pendown()
speed(10)
pensize(2)





def draw_star(size):
    fillcolor("yellow")
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

draw_star(50)


penup()
goto(50, 0)
pendown()


draw_star(50)
goto(0,0)

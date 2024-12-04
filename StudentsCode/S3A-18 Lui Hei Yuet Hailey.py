#paste your code here:

from turtle import *


def draw_sun():
    penup()
    goto(0, -100)
    pendown()
    color("yellow")
    begin_fill()
    circle(100)
    end_fill()
    
    
    for i in range(12):
        penup()
        goto(0, 0)
        pendown()
        forward(150)
        penup()
        goto(0, 0)
        right(30)


def draw_moon():
    penup()
    goto(50, 50)
    pendown()
    color("lightgray")
    begin_fill()
    circle(40)
    end_fill()

    
    penup()
    goto(30, 50)
    pendown()
    color("yellow")
    begin_fill()
    circle(23)
    end_fill()

speed(50)
bgcolor('black')
draw_sun()
draw_moon()

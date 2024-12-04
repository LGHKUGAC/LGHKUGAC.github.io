from turtle import *
import random
bgcolor('black')
color("lightblue")
speed(0) 
width(2)

def draw_star(size, color):
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def draw_hexagon(size, color):
    fillcolor(color)
    begin_fill()
    for _ in range(6):
        forward(size)
        right(60)
    end_fill()

def draw_circle(radius, color):
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def draw_complex_logo():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
    
    for i in range(12):
        penup()
        goto(0, 0)
        setheading(i * 30)
        forward(100)
        pendown()
        draw_star(30, random.choice(colors))
        penup()
        backward(100)

    for i in range(12):
        penup()
        goto(0, 0)
        setheading(i * 30 + 15) 
        forward(150)
        pendown()
        draw_hexagon(40, random.choice(colors))
        penup()
        backward(150)

    penup()
    goto(0, -50)
    pendown()
    draw_circle(70, random.choice(colors))

draw_complex_logo()
hideturtle()


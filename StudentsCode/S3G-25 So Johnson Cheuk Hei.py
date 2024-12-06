#paste your code here:
from turtle import *

def draw_petal(outline_color, size):
    pencolor(outline_color)
    fillcolor('black')
    begin_fill()
    
    for _ in range(2):
        forward(size)
        left(60)
        forward(size)
        left(120)
    
    end_fill()

def draw_flower(num_petals, layers):
    angle = 360 / num_petals

    for layer in range(layers):
        petal_size = 70 - (layer * 10)
        for _ in range(num_petals):
            outline_color = random.choice(['purple', 'red', 'orange', 'blue', 'green'])
            draw_petal(outline_color, petal_size)
            left(angle)

def setup_environment():
    speed(0)
    pensize(2)
    bgcolor('darkred')

def draw_flower_pattern():
    setup_environment()
    draw_flower(num_petals=10, layers=5)

    penup()
    goto(0, -20)
    pendown()
    fillcolor('yellow')
    begin_fill()
    circle(20)
    end_fill()

    hideturtle()

draw_flower_pattern()


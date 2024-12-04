from turtle import *
import random

number = 20
colors = ["wheat","coral", "khaki", "beige", "antiquewhite", "seashell", "mistyrose"]


bgcolor("black")
speed(0)
hideturtle()

def draw_circle(x, y, radius, color_name):
    penup()
    goto(x, y - radius)
    pendown()
    color(color_name)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    goto(0,0)
    

draw_circle(0, 0, 75, "white")


for i in range(number):
    x = random.randint(-150, 200)
    y = random.randint(-150, 100)
    size = random.randint(2, 5)
    colors_rand = random.choice(colors)
    draw_circle(x, y, size, colors_rand)

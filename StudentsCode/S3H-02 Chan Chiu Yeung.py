#paste your code here:

from turtle import *

def draw_shape(color_fill, pen_color, size=50, sides=8):
    pensize(16)
    fillcolor(color_fill)
    color(pen_color)
    
    for _ in range(sides):
        left(45)
        for _ in range(sides):
            forward(size)
            right(45)
    
speed(0)
bgcolor("black")
draw_shape('#00fff0', '#00fff0')
    
forward(13)
draw_shape('#00c1ff', '#00c1ff')
    
forward(13)
draw_shape('#0c00ff', '#0c00ff')
    
forward(13)
draw_shape('#5d16c2', '#5d16c2')
    




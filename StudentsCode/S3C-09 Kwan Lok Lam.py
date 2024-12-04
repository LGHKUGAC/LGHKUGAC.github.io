from turtle import *
import random

# Generate random RGB values and return them as a hex string
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))
  
# Function to draw a bolt body
def draw_bolt_body(x, y, ratio):
    penup()
    pensize(140 * ratio)
    goto(x, y)
    setheading(90)
    colors = ["#FFD700", "#FFEC8B", "#FFD700"]

    segments = 30
    segment_height = 300 / segments
    for i in range(segments):
        color = colors[i % len(colors)]
        pencolor(color)
        penup()
        goto(x, y + i * segment_height)
        pendown()
        forward(segment_height * ratio)


# Function to draw a bolt head
def draw_bolt_head(x,y,ratio,angle):
    penup()
    goto(x, y)
    pendown()
    right(180)
    for i in range(120):
        pencolor(random_color())
        forward(i * ratio)
        left(angle)


# Function to draw a filled lightning bolt
def draw_lightning(x,y,shapeColor,ratio):
    pensize(5)
    penup()
    goto(x,y)    
 
    fillcolor(shapeColor)
    begin_fill()
    setheading(60)
    forward(300 * ratio)
    right(120)
    forward(130 * ratio)
    left(120)
    forward(200*ratio)
    end_fill()


#Change background color
bgcolor("black")


#Set up turtle
speed(0)


# Create a bolt body

draw_bolt_body(0, -250, 0.6)

width(25)
# Create the bolt head
draw_bolt_head(0, 50, 0.8, 61)


# Draw the filled lightning bolt icon 1
draw_lightning(83,78, 'black',0.2)
draw_lightning(80,80, 'yellow',0.2)

# Draw the filled lightning bolt icon 2
draw_lightning(113,48, 'black',0.15)
draw_lightning(110,50, 'yellow',0.15)


# Hide the turtle 
hideturtle()

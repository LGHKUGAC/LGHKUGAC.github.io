from turtle import Screen, Turtle
import random
import math



# List of turtle colors
# List of projector-friendly and visually pleasing colors
turtle_colors = [
    "red", "blue", "green", "yellow", "purple", "orange",
    "cyan", "magenta", "gold", "lightblue", "lightgreen", "pink"
]



# Function to pick a random color
def pick_random_color_():
    return random.choice(turtle_colors)


# Create a single Screen instance
_screen = Screen()
_turtle = Turtle()


# Global variable to store color mode
_color_mode = 255  # Default color mode set to 255 for compatibility

def fd(distance):
    return _turtle.forward(distance)


def bk(distance):
    return _turtle.backward(distance)

def pu():
    return _turtle.penup()

def pd():
    return _turtle.pendown()

def lt(angle):
    return _turtle.left(angle)


def rt(angle):
    return _turtle.right(angle)
def up():
    return _turtle.penup()


def down():
    return _turtle.pendown()


def width(size):
    return _turtle.pensize(size)


def setpos(x, y=None):
    return _turtle.goto(x, y)


def setposition(x, y=None):
    return _turtle.goto(x, y)


def seth(to_angle):
    return _turtle.setheading(to_angle)


# Function to simulate colormode
def colormode(mode=None):
    global _color_mode
    if mode is not None:
        if mode == 1.0 or mode == 255:
            _color_mode = mode
        else:
            raise ValueError("colormode must be either 1.0 or 255")
    return _color_mode


# Function to scale colors based on the current color mode
def _scale_color(color):
    if isinstance(color, tuple):
        return tuple(c / _color_mode for c in color)
    elif isinstance(color, int) or isinstance(color, float):
        return color / _color_mode
    else:
        return color  # Assume string color names are acceptable

def color(*args):
    pencolor(*args)
    fillcolor(*args)

def pencolour(*args):
    pencolor(*args)

# Redefine color-related functions to handle scaling
def bgcolor(*args):
    scaled_args = [_scale_color(arg) for arg in args]
    return _screen.bgcolor(*scaled_args)


def pencolor(*args):
    scaled_args = [_scale_color(arg) for arg in args]
    return _turtle.pencolor(*scaled_args)


def fillcolor(*args):
    scaled_args = [_scale_color(arg) for arg in args]
    return _turtle.fillcolor(*scaled_args)

def fillcolour(*args):
    scaled_args = [_scale_color(arg) for arg in args]
    return _turtle.fillcolor(*scaled_args)


# Redefine other commonly used turtle functions
def speed(*args, **kwargs):
    return _turtle.speed(*args, **kwargs)


def pensize(size):
    return _turtle.pensize(size)


def penup():
    return _turtle.penup()


def pendown():
    return _turtle.pendown()


def goto(x, y=None):
    return _turtle.goto(x, y)


def forward(distance):
    return _turtle.forward(distance)


def backward(distance):
    return _turtle.backward(distance)


def left(angle):
    return _turtle.left(angle)


def right(angle):
    return _turtle.right(angle)


def circle(radius, extent=None, steps=None):
    return _turtle.circle(radius, extent, steps)


def begin_fill():
    return _turtle.begin_fill()


def end_fill():
    return _turtle.end_fill()


def setheading(to_angle):
    return _turtle.setheading(to_angle)


def home():
    return _turtle.home()


def dot(size=None, *color):
    scaled_color = [_scale_color(c) for c in color]
    return _turtle.dot(size, *scaled_color)


def hideturtle():
    return _turtle.hideturtle()


def showturtle():
    return _turtle.showturtle()


# Update the default turtle to be the one we created
turtle = _turtle

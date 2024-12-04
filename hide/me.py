from turtle import *
import math

# TURTLE TEST
# Constants
pencolor('white')
bgcolor('black')
INVERSESQRTTWO = 1 / math.sqrt(2)
MAX = 6  

def createRec(position, angle, size):
    pencolor(pick_random_color_())
    penup()
    goto(position)
    setheading(angle)
    pendown()
    for _ in range(4):
        forward(size)
        left(90)

def drawRecursion(position, angle, size, count):
    if count > MAX:
        return
    
    # Draw the current square
    createRec(position, angle, size)
    
    # Calculate the new size for the child squares
    new_size = size * INVERSESQRTTWO
    
    # Calculate position for the left child square
    x, y = position
    x1 = x + size * math.cos(math.radians(angle + 90))
    y1 = y + size * math.sin(math.radians(angle + 90))
    left_angle = angle + 45
    drawRecursion((x1, y1), left_angle, new_size, count + 1)
    
    # Calculate position for the right child square
    x2 = x + size * math.cos(math.radians(angle))
    y2 = y + size * math.sin(math.radians(angle))
    right_angle = angle - 45
    drawRecursion((x2, y2), right_angle, new_size, count + 1)

def createRecursionStart(size):
    # Initial position and count
    initial_pos = (-100, -100)
    # Starting from the top of the initial square
    x, y = initial_pos
    x_top = x
    y_top = y + size
    drawRecursion((x_top, y_top), 0, size, 1)

def main():
    speed('fastest')
    hideturtle()
    createRecursionStart(60)
    done()
    
main()

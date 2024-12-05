#paste your code here:

import turtle

def spirograph(size, angle):
    bgcolor("black")  # Set background color to black
    pencolor("white")  # Set pen color to white

    penup()
    goto(0, -size/2)
    pendown()
    speed(0)

    for _ in range(360 // angle):
        circle(size/2)
        left(angle)

    hideturtle()

spirograph(100, 5)


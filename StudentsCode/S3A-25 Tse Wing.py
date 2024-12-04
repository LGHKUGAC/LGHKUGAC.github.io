#paste your code here:

from turtle import *
                                                                                                                                                                                                   
speed(0)


def draw_petal(colour):
    pencolor(colour)
    for i in range(4):
        forward(60)
        left(90)
       
bgcolor('black')
pensize(4)
color('gray')
fillcolor('skyblue')


begin_fill()

a = 20  
x = 360 / a  
for i in range(a):
    draw_petal('black')
    left(x)


blue = 255
green = 210
red = 229


def draw_circles_around():
    pencolor(blue,green,red)  
    penup()  
    radius = 90  
    for i in range(a):
        goto(0, 0) 
        forward(radius)  
        pendown()  
        circle(20)  
        penup() 
        goto(0, 0) 
        left(x)
      


end_fill()
        
def draw_radiating_lines(length):
    pencolor('lightyellow')
    for i in range(a):
        penup()
        goto(0, 0)  
        setheading(i * x) 
        pendown()
        forward(length) 
        penup()
        goto(0, 0) 

draw_circles_around()
draw_radiating_lines(150) 


hideturtle()



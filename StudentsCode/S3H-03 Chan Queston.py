#paste your code here:import random

from turtle import *

def draw_logo(colour):
    pencolor(colour)
    for i in range(4):
        forward(60)
        left(90)


pensize(5)
bgcolor('black')  
fillcolor('white')  
vine = 13
staff = 360 / vine


speed(0)  

begin_fill()
for i in range(vine):
    draw_logo('gold')
    left(staff)
end_fill()

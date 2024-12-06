#paste your code here:
from turtle import *
bgcolor('darkblue')
speed(7)
angle = 360 / 7 
skip = 2 
colors_list = ["hotpink", "violet","mediumorchid", "mediumslateblue","royalblue", "dodgerblue", "deepskyblue"]
penup()
goto(-45, 45)
pendown()
for i in range(7):
    pensize(7)
    color(colors_list[i % len(colors_list)]) 
    forward(100)  
    right(angle * skip)
penup()
goto(5, -72)  
setheading(0)  
pendown()
pensize(7) 
color("mediumslateblue")  
circle(80)
hideturtle()



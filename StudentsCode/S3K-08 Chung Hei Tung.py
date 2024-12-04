from turtle import *

def draw_star():
    fillcolor(252, 202, 70)
    begin_fill()
    speed(0)
    left(45)
    for _ in range(6):
        forward(60)
        left(150)
        forward(35)
        left(60)
        forward(35)
        left(120)
        forward(35)
        left(60)
        forward(35)
        penup()
        left(180)
        forward(35)
        right(60)
        forward(35)
        left(150)
        pendown()
    end_fill()

def draw_additional_stars():
    
    speed(0)
    
    small_star_positions = [
        (100, 0), 
        (-100, 0), 
        (0, 100), 
        (0, -100), 
        (70, 70), 
        (-70, -70),
        (70, -70), 
        (-70, 70)
    ]
    
    for pos in small_star_positions:
        penup()
        goto(pos)
        setheading(0)  
        pendown()
        fillcolor(255, 223, 86)  
        begin_fill()
        for _ in range(5):  
            forward(30)
            left(144)
        end_fill()

def draw_eight_point_star(position):
    
    penup()
    goto(position)
    setheading(0)
    pendown()
    fillcolor("#feffa6")
    begin_fill()
    for _ in range(8):
        forward(20)
        left(135)  
    end_fill()

def draw_dots():
   
    speed(10)  
    dot_positions = [
        (120, 50), 
        (120, -50), 
        (-120, 50), 
        (-120, -50), 
        (50, 120), 
        (-50, 120), 
        (50, -120), 
        (-50, -120)
    ]
    
    for pos in dot_positions:
        penup()
        goto(pos)
        pendown()
        dot(5, "#fffa86")  

def draw_logo():
    
    bgcolor(35, 61, 77)  
    draw_star()  
    draw_additional_stars()  
    draw_dots()  
    speed(0)

    
    eight_point_star_positions = [
        (150, 100), 
        (150, -100), 
        (-150, 100), 
        (-150, -100), 
        (100, 150), 
        (-100, 150), 
        (100, -150), 
        (-100, -150)
    ]
    
    for pos in eight_point_star_positions:
        draw_eight_point_star(pos)

    hideturtle()  


draw_logo()


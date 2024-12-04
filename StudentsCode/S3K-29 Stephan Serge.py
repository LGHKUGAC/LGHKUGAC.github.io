#paste your code here:

from turtle import *

speed(0)

pensize(5)

bgcolor('black')

def draw_b(radius_of_circle):
  pencolor('white')
  penup()
  goto(-125, 50)
  pendown()
  circle(radius_of_circle, 180)
  right(180)
  circle(radius_of_circle, 180)
  left(90)
  forward(radius_of_circle * 4)

draw_b(15)

def draw_l(length1, length2):
  penup()
  goto(-75, 115)
  pendown()
  forward(length1)
  left(90)
  forward(length2)

draw_l(70, 20)

def draw_a(length):
  penup()
  goto(0, 120)
  pendown()
  right(80)
  forward(length)
  forward(-length)
  right(20)
  forward(length)
  forward(-length / 2.5)
  left(105)
  forward(length / 4.8)
  
draw_a(80)

def draw_z(length1, length2):
  penup()
  goto(50, 120)
  pendown()
  right(5)
  forward(length1)
  right(130)
  forward(length2)
  left(130)
  forward(length1)

draw_z(50, 100)

def draw_e(length1, length2):
  penup()
  goto(125, 120)
  pendown()
  forward(length1)
  forward(-length1)
  for i in range(2):
    right(90)
    forward(length2)
    left(90)
    forward(length1)
    forward(-length1)
    
draw_e(50, 35)

pensize(3)

def draw_circle(length1, length2, color1, color2, num_of_loops):
  penup()
  goto(-100, -60)
  pendown()
  turn_angle = 360 / num_of_loops / 2
  for i in range(num_of_loops):
    pencolor(color1)
    forward(length1)
    right(90)
    fillcolor(color2)
    begin_fill()
    circle(10)
    end_fill()
    left(90)
    backward(length1)
    right(turn_angle)
    pencolor(color2)
    forward(length2)
    backward(length2)
    right(turn_angle)

draw_circle(35, 25, 'red', 'coral', 10)

def draw_square(length1, length2, color1, color2, num_of_loops, square_length):
  penup()
  goto(-45, -60)
  pendown()
  forward(20)
  penup()
  goto(15, -60)
  pendown()
  turn_angle = 360 / num_of_loops / 2
  for i in range(num_of_loops):
    pencolor(color1)
    forward(length1)
    right(90)
    fillcolor(color2)
    begin_fill()
    forward(square_length / 2)
    left(90)
    for i in range(3):
      forward(square_length)
      left(90)
    forward(square_length / 2)
    end_fill()
    left(90)
    backward(length1)
    right(turn_angle)
    pencolor(color2)
    forward(length2)
    backward(length2)
    right(turn_angle)
    
draw_square(30, 20, 'green', 'blue', 12, 10) 

def draw_triangle(length1, length2, color1, color2, num_of_loops, triangle_length):
  penup()
  goto(55, -60)
  pendown()
  goto(75, -60)
  penup()
  goto(125, -60)
  pendown()
  turn_angle = 360 / num_of_loops / 2
  for i in range(num_of_loops):
    pencolor(color1)
    forward(length1)
    right(90)
    fillcolor(color2)
    begin_fill()
    forward(triangle_length / 2)
    left(120)
    for i in range(2):
      forward(triangle_length)
      left(120)
    forward(triangle_length / 2)
    end_fill()
    left(90)
    backward(length1)
    right(turn_angle)
    pencolor(color2)
    forward(length2)
    backward(length2)
    right(turn_angle)  
    
draw_triangle(40, 30, 'cyan', 'purple', 16, 10)


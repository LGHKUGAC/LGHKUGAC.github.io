#paste your code here:

from turtle import*


bgcolor('black')
speed(10)
pensize(2)
pencolor("black")

def pattern():
  fillcolor("yellowgreen")
  penup()
  home()
  pendown()
  
  begin_fill()
  pencolor("yellowgreen")
  setheading(90)
  goto(-75, -32.5)
  
  for x in range(6):
    circle(50, 60)
    right(120)
    circle(50, 60)
    right(60)
  end_fill()
  
    
    
def draw_circle(x, y, radius, fill_color=None):
  penup()
  goto(x, y - radius)
  pendown()
  
  if fill_color:
    fillcolor(fill_color)
    begin_fill()
    
  circle(radius)
  
  if fill_color:
    end_fill()
  
def turtlepattern():
  penup()
  goto(0,-50)
  setheading(0)
  pendown()
  
  for i in range(6):
    penup()
    goto(0,0)
    setheading(60 * i)
    forward(20)
    pendown()
    
    fillcolor("darkgreen")
    begin_fill()
    circle(15, 180)
    left(90)
    forward(30)
    left(90)
    circle(15, 180)
    left(90)
    forward(30)
    end_fill()
    
def draw_turtle():
  #shell
  draw_circle(50, 50, 50, "darkolivegreen")
  
  #head
  draw_circle(20, 85, 20, "mediumseagreen")
  #legs
  draw_circle(-40, 40, 15, "forestgreen")
  draw_circle(70, 40, 15, "forestgreen")
  draw_circle(-20, -35, 15, "forestgreen")
  draw_circle(50, -35 , 15, "forestgreen")
  #tail
  draw_circle(10 ,-45, 10, "seagreen")
  
  #eyes
  draw_circle(-2.5, 77.5, 5, "black")
  draw_circle(12.5, 77.5, 5, "black")
  
  
  #smile
  penup()
  goto(-9,60)
  pendown()
  setheading(-60)
  circle(10, 120)

  
pattern()
draw_turtle()
turtlepattern()

#brief introduction:
#in this logo, the seablue background is the ocean and theres a seaturtle inside. The lightgreen symbolises the trouble that the turtles are in, 
#they face the problem of intnsive plastic waste everyday and struggles to survive. And ultimately, the half-circles in the turtle's shell 
#indicates how uch plastic the turtle has eaten and how their problem should be given more attention. 



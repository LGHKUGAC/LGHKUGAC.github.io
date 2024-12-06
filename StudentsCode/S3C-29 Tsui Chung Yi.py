#paste your code here:
from turtle import *

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
speed(0)
          
#gradient background colors
def change_colors():
  r = 255
  g = 255
  b = 255
  for i in range(255):
    color(r, g, b)
    g -= 1
    b -= 1
    fd(450)
    bk(450)
    left(90)
    fd(1.5)
    right(90)

#drawing a star
def draw_star(size):
    for i in range(5):
        forward(size)
        right(144)

#drawing multiple stars
def draw_more_stars(num_stars, size):
    for i in range(num_stars):
        draw_star(size)
        right(360 / num_stars)  
        
#getting in place to draw the background
penup()
goto(-200, -150)
pendown()
change_colors()

#getting in place to draw the stars
penup()
goto(0,0)
pendown()
color("yellow")  
fillcolor("black")
begin_fill()
draw_more_stars(30, 100)
end_fill()



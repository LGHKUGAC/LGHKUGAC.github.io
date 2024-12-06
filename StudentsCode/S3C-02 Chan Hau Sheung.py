#paste your code here:

from turtle import *
def square(size):
  angle = 360/4
  for i in range(6):
    forward(size)
    left(angle)
side_length = 35
# the idea of my logo:          
# For the logo, l tend to create something which can provide a vibrant atmosphere and the sense of growth at the first impression to the viewers,
#which ultimately lead me to brainstorm a logo related to plants/flowers, an element which offen let people think of sunshine and growth. 
# I made up a red-coloured flower, combined with a fresh-green branch and a gold-coloured anther which is the 
#yellow sac-like structure located at the top of the flower in nature, to show the sense of hope for the logo.
speed(10)
pensize(5)
pencolor('darkred')
fillcolor('gold')
bgcolor('lightblue')
begin_fill()
for i in range(3):
  square(side_length)
  right(360/3)
end_fill()
side_length = 35
pensize(5)
pencolor('darkred')
fillcolor('gold')
bgcolor('lightblue')
begin_fill()
for i in range(3):
  square(side_length)
  right(360/3) 
end_fill()
pensize(10)
pencolor('darkgreen')
right(90)
penup ( )
forward(7)
pendown ( )
forward(110)  
penup ( )  
right(180)
forward(65)
pendown ( )
right(90)
forward(18)
right(90)
forward(18)
right(90)
forward(18)  





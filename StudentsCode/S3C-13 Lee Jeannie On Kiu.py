#paste your code here:
from turtle import *
#logo (Non-interactive)
bgcolor("black")
speed(0)
pensize(2)
def drawlogo(size):
  #Draw the background circle
  penup()
  goto(-(size*9/10),-(size*6/10))
  right(90)
  forward(size*6.2)
  left(90)
  pencolor('white')
  fillcolor(3, 35, 87)
  begin_fill()
  pendown()
  circle(size*6)
  end_fill()
  penup()
  goto(0,0)
  #Prepare to draw the wreaths
  pencolor("black")
  times = 0
  wreaths = 0
  for i in range (3):
    wreaths = wreaths + 1
    for i in range (8):
      for i in range (3):
        #Draw flower 3 times
        times = times + 1
        penup()
        circle(size, 360-i)
        pendown()
        #To change colour for each petal
        fillcolor(3, 252-(2.5*times), 252)
        begin_fill()
        circle(size, 75)
        left(90)
        circle(size,75)
        end_fill()
      #Prepare for the second flower
      penup()
      left(50)
      forward(size*(3/2))
    #Where the turtle needs to move to prepare for the second wreath
    if wreaths == 1:
      goto(-size*2,-size*4)
    elif wreaths == 2:
      goto(size*3,-size*3.7)
      
trusize = 20

drawlogo(trusize)


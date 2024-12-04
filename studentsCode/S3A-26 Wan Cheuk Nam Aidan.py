#paste your code here:
from turtle import *

def dflower():
  for i in range(10):

    right(90)
    speed(0)
    pencolor (pick_random_color_())
    fillcolor (pick_random_color_())
    circle(20)
  
bgcolor('black')
dflower()
goto(-10,20)
dflower()
goto(10,20)
dflower()
goto(20,10)
dflower()
goto(20,20)
dflower()
goto(20,80)
dflower()


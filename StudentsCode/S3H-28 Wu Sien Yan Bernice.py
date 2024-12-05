#paste your code here:
from turtle import *
speed(0)
begin_fill()
end_fill()
penup()
pendown()

def draw():
  for i in range (50):
    
    forward(75)
    right(90)
    forward(30)
    right(80)
    forward(70)

goto(-100,100)  
pencolor('hotpink')
draw()
goto(100,100)
pencolor('royalblue')
draw()
goto(50,50)
pencolor('orchid')
draw()
goto(-50,-30)
pencolor('darkviolet')
draw()
goto(130,-40)
pencolor('navy')
draw()
goto(-125,-50)
pencolor('yellow')
draw()



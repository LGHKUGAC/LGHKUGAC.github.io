#paste your code here:
from turtle import *

bgcolor('black')

speed(10)

x = 1 
speed(0) 
goto(-24,24)
while x < 185: 

  r = random.randint(0,255) 
  g = random.randint(0,255)  
  b = random.randint(0,255) 

  colormode(255)  
  pencolor(r,g,b) 
  fd(50 + x) 
  rt(90.991) 

  x = x+1 


color('gold')
width(5)

penup()
goto(0,0)
pendown()
for i in range(8):
  penup()
  forward(10)
  pendown()
  forward(15)
  penup()
  goto(0,0)
  left(45)

color('gray')  
width(3)
forward(10)
left(90)
pendown()
circle(10,90)
penup()
goto(0,0)
forward(10)
left(90)
pendown()
circle(10,90)
left(90)
pendown()
forward(20)
penup()
goto(0,0)
left(90)
forward(10)
right(180)
pendown()
forward(20)


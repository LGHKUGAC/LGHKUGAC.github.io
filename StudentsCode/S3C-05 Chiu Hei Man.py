#paste your code here:
from turtle import *
speed(20)
bgcolor('black')

def thing(x,y,angle): #to define the function used for making the small blue rhombuses 
  penup()
  goto(0,0)
  goto(x,y)
  left(angle)
  forward(50)
  pensize(3)
  pencolor(107, 134, 155)
  fillcolor(179,206,229)
  pendown()
  begin_fill()
  left(27.5)
  forward(20)
  right(55)
  forward(20)
  right(125)
  forward(20)
  right(55)
  forward(20)
  end_fill()
  right(360-angle)

# to make the big circle
pensize(3)
pencolor(168, 127, 126)
fillcolor(247,202,201)
begin_fill()
penup()
forward(100)
left(90)
pendown()
circle(100)
end_fill()

for i in range(4): # to make the 4 small circles
  fillcolor(168, 127, 126)
  begin_fill()
  circle(45)
  end_fill()
  circle(100, extent = 90)
  
for i in range(4): # to make the big star, the center of the logo
  pensize(3)
  pencolor(65,32,169)
  fillcolor(161,169,254)
  penup()
  goto(0,0)
  pendown()
  begin_fill()
  left(45)
  forward(40)
  left(72.5)
  forward(60)
  left(125)
  forward(60)
  left(72.5)
  forward(40)
  end_fill()

  goto(0,0)
  fillcolor(43, 20, 117)
  begin_fill()
  left(134)
  forward(80)
  right(151.5)
  forward(60)
  right(72.5)
  forward(40)
  end_fill()
  left(45)
  
# to make the small blue rhombuses
thing(-5,5,45)

penup()
goto(0,0)
pendown()

thing(2,-6,345)

penup()
goto(0,0)
pendown()

thing(8,1.5,312.5)

penup()
goto(0,0)
pendown()

thing(-3,-3,70)

penup()
goto(0,0)
pendown()



#paste your code here:

from turtle import *
speed(10)
bgcolor('black')
# define a function to draw one 3-circle shape
def shape(no): 
  pencolour(255,125,b) #making the pen colour of the 3-circle shape changeable
  pensize(3)  
  circle(30)
  goto(0,0)    
  circle(45)
  goto(0,0)
  circle(50)
  return shape
  
#repeat drawing one 3-circle shape and another 3-circle shape with colour three times
if __name__ == "__main__": 
  for i in range(3):
    b = 110+(40*i) #let the colour of 3-circle shape be gradient
    shape(1)
    left(60)    
    fillcolour('#ffdab9')
    begin_fill()
    shape(1)
    end_fill()
    left(60)

#draw one more 3-circle shape to make the logo look better
right(120)
b=160
shape(1)

#goto the side of the six 3-circle shape and draw six small circles
penup()
goto(-120,0)
left(30)
pencolor('#F98B88')
for i in range(6):
  circle(120,60)
  pendown()
  circle(15)
  penup()

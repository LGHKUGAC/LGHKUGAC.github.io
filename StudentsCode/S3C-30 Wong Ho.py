#paste your code here:
from turtle import *
#blue gradient fuction
def blue_gradient(red, green, blue):
  pu()
  goto(-200,-150)
  pd()
  for i in range(255):
    pencolor(red, green, blue)
    red = red - 1
    green = green - 1 
    fd(600)
    bk(600)
    lt(90)
    fd(2)
    rt(90)  
#red gradient fuction
def red_gradient(red, green, blue):
  pu()
  goto(-200,-150)
  pd()
  for i in range(255):
    pencolor(red, green, blue)
    blue = blue - 1
    green = green - 1 
    fd(600)
    bk(600)
    lt(90)
    fd(2)
    rt(90) 
#green gradient fuction
def green_gradient(red, green, blue):
  pu()
  goto(-200,-150)
  pd()
  for i in range(255):
    pencolor(red, green, blue)
    blue = blue - 1
    red = red - 1 
    fd(600)
    bk(600)
    lt(90)
    fd(2)
    rt(90)  

speed(0)
blue_gradient(255,255,255)
#Move to the right position
pu()
home()
rt(90)
fd(40)
lt(90)
pd()
pencolor(0,0,0)
#Start making the thing
r = 1
fillcolor('pink')
begin_fill()
for i in range(100):
  sr = 360 / 100
  rt(sr),
  circle(r),
  r += 1
  pu,
  home,
  pd,
end_fill()



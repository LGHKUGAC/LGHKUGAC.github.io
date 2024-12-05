#paste your code here:
from turtle import *
def sun ():
  forward(50)
  right(150)
  forward(50)
  right(150) 
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150) 
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150)
  forward(50)
  right(150)
  
speed(0)
#loop = int(input('How many loops? '))

for i in range (8):
  begin_fill()
  sun ()
  left(45)
  penup( )
  forward(20)
  
  pendown()
  fillcolour('gold')
  end_fill()
  bgcolor('black')
  
  


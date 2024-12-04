from turtle import *

speed(20)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)


fillcolor('plum') 
begin_fill()
pensize(5)
pencolor('yellow')

for i in range (8):           
  petal=draw_petal('plum')
  
  left(45)
end_fill()

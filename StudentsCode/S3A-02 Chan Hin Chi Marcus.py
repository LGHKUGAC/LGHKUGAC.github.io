#paste your code here:

from turtle import *
spokes = 40  
angle = 179 / spokes
speed(0)

bgcolor('black')
pencolor('red')
for i in range(spokes):
  forward(110)
  backward(110)
  left(angle)

left(angle / 2 )

pencolor('gold')
for i in range(spokes):
  forward(120)
  backward(120)
  left(angle)
  
  left(angle / 2 )

pencolor('orange')
for i in range(spokes):
  forward(120)
  backward(120)
  left(angle)
  
  pencolor('orange')
for i in range(spokes):
  forward(120)
  backward(120)
  left(angle)




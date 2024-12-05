#paste your code here:

from turtle import *
speed(0)
bgcolor('black')
pensize(3)
fillcolor('skyblue')
spokes = 10
angle = 360 / spokes


pencolor('lightyellow')
for i in range(spokes):
  forward(90)
  backward(90)
  left(angle)
  
left(angle / 2)

num_shapes = 5

degrees = 360/num_shapes 

pencolor('mistyrose')
for i in range(num_shapes): 
  for s in range(4):
    forward(50)
    right(90)
  right(degrees)
  
begin_fill()

pencolor('cornflowerblue')
circle(40)
  
end_fill()

forward(30)

fillcolor('white')
begin_fill()

pencolor('lightgrey')
circle(30)

end_fill()

left(10)
num_shapes = 5

degrees = 360/num_shapes 

pencolor('mistyrose')
for i in range(num_shapes): 
  for s in range(4):
    forward(50)
    right(90)
  right(degrees)

pencolor('lightpink')
sides = 9
angle = 360 / sides

pensize(5)
for s in range(7):
  forward(10)
  backward(10)
  left(30)
  forward(10)
  backward(10)
  left(30)










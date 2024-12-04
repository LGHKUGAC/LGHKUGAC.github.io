#paste your code here:


from turtle import *
pensize(3)
red = 160
green = 130
blue = 230
bgcolor('royalblue')
pencolor('white')
fillcolor(red,green,blue)
begin_fill()
speed(10)

num_shapes = 8
for i in range(num_shapes): 
  for s in range(4): 
    forward(50)
    right(90)
  right(45)

end_fill()



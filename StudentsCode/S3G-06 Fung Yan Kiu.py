bgcolor('black')
speed(6)
pensize(3)
pencolor('lightcyan')
fillcolor('paleturquoise')
begin_fill()
angle= 360/8 
for i in range(8):
    left(angle)
    forward(50)  
end_fill()      
left(90)
penup()
forward(50)
left(90)
forward(50)
pendown()

pencolor('mediumblue')
pensize(5)
for i in range(7):
  forward(50)
  backward(50)
  left(30)
  
penup()
right(30)
left(90)
forward(20)
right(90)
pendown()

for i in range(7):
  forward(50)
  backward(50)
  left(30)


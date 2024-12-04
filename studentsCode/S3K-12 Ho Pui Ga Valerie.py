#paste your code here:


from turtle import *
speed(0)
def square(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)
bgcolor('darkblue')
pensize(5)
pencolor('RosyBrown')

r = 2
        
for s in range (2, 20, 2):
  circle(r)
  r = r+8
left(90)  
t = 2
for s in range (2, 20, 2):
  circle(t)
  t = t+5
right(180)
t = 2
for s in range (2, 20, 2):
  circle(t)
  t = t+5

pencolor('DarkOliveGreen')
fillcolor('DarkOliveGreen')

pensize(3)
penup()
forward(50)
pendown()
begin_fill()
circle(70,180,4)
left(150)
forward(50)
right(30)
forward(40)
right(50)
forward(50)
right(30)
forward(52)
end_fill()

begin_fill()
left(100)
forward(66)
right(40)
forward(40)
right(40)
forward(40)
right(40)
forward(40)
right(170)
forward(40)
left(40)
forward(40)
left(40)
forward(40)
left(30)
forward(50)

end_fill()



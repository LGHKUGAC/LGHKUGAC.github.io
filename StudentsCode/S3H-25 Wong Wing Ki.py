#paste your code here:


from turtle import *
speed(10)

def pedal(color):
  pencolor(color)
  for i in range(4):
    circle(10+i*5)


pensize(3)
bgcolor('black')
fillcolor('hotpink')
angles=360/5
begin_fill()

for i in range(5):
  pedal('purple')
  left(angles)
end_fill()




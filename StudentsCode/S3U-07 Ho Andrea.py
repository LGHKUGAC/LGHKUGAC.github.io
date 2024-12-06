
#assigned numbers: 
## slices: 20
## petals: 20
speed(50)
from turtle import *
bgcolor('black')
#1
fillcolor('pink') 

begin_fill()

pencolor('salmon')
pensize(5)
left(45)

for i in range(3):
  forward(30)
  left(90)

forward (30)
right(45)
penup()
forward(5)
pendown()
left(-45)

for i in range(3):
  forward(30)
  left(90)
 
forward (30)
end_fill()

#2 
pencolor('gold')
pensize(4)
slices = 20


angle = 360 / slices

for i in range(slices):
 
  forward(110)
  backward(110)
  
  
  left(angle)

  
 
def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)
#3
pensize(5)

pet = 20
angle = 360/pet
begin_fill()
for i in range(pet):
  draw_petal('salmon')
  left(angle)
end_fill()

speed(0)



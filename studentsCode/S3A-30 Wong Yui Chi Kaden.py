#paste your code here:

from turtle import *
speed(20)
def random_color_generator():
  r = random.randint(10, 255)
  g = random.randint(10, 255)
  b = random.randint(10, 255)
  return (r, g, b)
pencolor (random_color_generator())
bgcolor('black')
for i in range(32):
  pencolor(random_color_generator())
  forward(130)
  backward(130)
  left(360/32)
pencolour (random_color_generator())
fillcolour (random_color_generator())
penup()
right(90)
forward(100)
left(90)
pendown()
begin_fill()
circle(100)
end_fill()
penup()
left(90)
forward(100)
right(90)
pencolour ('darkblue')
for i in range(4):
      fillcolour ('yellow')
      begin_fill()
      circle(40)
      end_fill()
      penup()
      left(90)
      forward(15)
      fillcolour ('lightblue')
      begin_fill()
      left(30)
      forward(50)
      right(120)
      forward(50)
      right(120)
      forward(50)
      end_fill()
      left(30)
      penup()
      forward(15)     
fillcolour(random_color_generator())
right(90)
forward(20)
left(90)
begin_fill()
circle(20)
end_fill()
left(90)
forward(15)


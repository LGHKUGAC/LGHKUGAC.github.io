#paste your code here:

from turtle import *

#a = int(input("Radius: "))
a=25
speed(0)
pencolor(pick_random_color_())
pensize(5)
fillcolor(pick_random_color_())
begin_fill()
circle(a)
b = 360/a
for i in range(a-1):
  left(b)
  penup()
  forward(a)
  pendown()
  circle(a)
penup()


end_fill()

goto(-(a/2),a*4)
seth(90)
pendown()
bgcolor('black')
pencolor(pick_random_color_())
for i in range(12):
  forward(a*1.5)
  backward(a*1.5)
  left(30)
left(15)
pencolor(pick_random_color_())
for i in range(12):
  forward(a*1.5)
  backward(a*1.5)
  left(30)





#paste your code here:

from turtle import *
speed = (5)
bgcolor('midnightblue')
n = 0
right(45)
for i in range(70,20,-10):
  goto(n,-n)
  pencolor('azure')
  dot(i)
  goto(n,-n)
  pencolor('midnightblue')
  forward(8)
  dot(i-3)
  n += 3
pencolor('paleturquoise')
dot(15)
pensize(8)
forward(92)
penup()
forward(1000)


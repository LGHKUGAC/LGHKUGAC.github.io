#paste your code here:
from turtle import *
speed(9)
  
bgcolor("#483D8B")
radius = 50
for i in range(20):
  pencolor("#00BFFF")
  circle(radius)
  left(5)
for i in range(20):
  pencolor("#FF69B4")
  circle(radius)
  left(5)
for i in range(20):
  pencolor("#9370DB")
  circle(radius)
  left(5)
for i in range(15):
  pencolor("#FFD700")
  circle(radius)
  left(5)
def square(half_length):
  left(90)
  forward(half_length)
  left(90)
  forward(half_length*2)
  left(90)
  forward(half_length*2)
  left(90)
  forward(half_length*2)
  left(90)
  forward(half_length)


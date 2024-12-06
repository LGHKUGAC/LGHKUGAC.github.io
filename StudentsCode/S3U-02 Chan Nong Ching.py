#paste your code here:
from turtle import *
bgcolor('black')
speed(0)
k = 8

n = 1
goto(-4, 57)
def change_color():
    R = random.randint(1, 255)
    B = random.randint(1, 255)
    G = random.randint(1, 255)
    pencolour(R, G, B)
for i in range(k*k*k):
  change_color()
  forward(n+1)
  right(n+1)
  n = n+1
pendown()
pencolour('black')
bgcolor('black')



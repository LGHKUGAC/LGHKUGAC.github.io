#paste your code here:

from turtle import *

def drawright(times):
  for i in range(times):
    forward(60)
    right(360/times)

def drawleft(times):
  for i in range(times):
    forward(60)
    left(360/times)

speed(10)
a=random.randint(80,255)
b=random.randint(80,255)
c=random.randint(80,255)
pensize(1)
bgcolor(a,b,c)
d=random.randint(0,255)
e=random.randint(0,255)
f=random.randint(0,255)
fillcolor(d,e,f)
begin_fill()
x = random.randint(5,7)
for i in range(4):
  drawright(x)
  left(90)
  drawleft(x)
end_fill()


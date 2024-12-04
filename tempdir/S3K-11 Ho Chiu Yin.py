#paste your code here:

from turtle import *
l = 70 
#length
o = l * 7/8
#width
m = l/4 

n = m + o
v = n + m
p = v/5

speed(10)
bgcolor('black')
pencolor('plum')
fillcolor('plum')
begin_fill()
right(30)
for s in range(2):
  forward(o)
  left(120)
  forward(l)
  left(60)
end_fill()
right(120)

pencolor('paleturquoise')
fillcolor('paleturquoise')
begin_fill()

for s in range(2):
  forward(o)
  right(120)
  forward(l)
  right(60)
end_fill()  
pencolor('seashell')
fillcolor('seashell')
begin_fill()

for s in range(2):
  forward(o)
  left(120)
  forward(o)
  left(60)
end_fill()

pencolor('plum')
fillcolor('plum')
penup()
forward(n)
pendown()
begin_fill()

right(120)
forward(v)
right(120)
forward(n)
right(60)
forward(p)
right(120)
forward(o)
left(120)
forward(m)
left(60)
forward(o)

right(60)
forward(p)
right(120)
forward(o)
left(120)
forward(p)
left(60)
forward(o)

right(60)
forward(p)
right(120)
forward(n)
end_fill()

penup()
right(60)
forward(v)
right(60)
pendown()

pencolor('seashell')
fillcolor('seashell')
begin_fill()
p = n/5

forward(n)
right(60)
forward(p)
right(120)
forward(p*2)
left(120)
forward(p*3)
left(60)
forward(p*2)
right(60)
forward(p)
right(120)
forward(n)
right(60)
forward(p)
right(120)
forward(p*2)
left(120)
forward(p*3)
left(60)
forward(p*2)

end_fill()

penup()
left(120)
forward(n-p)
right(60)
pendown()
pencolor('paleturquoise')
fillcolor('paleturquoise')
begin_fill()

forward(v)
left(120)
forward(n)
left(60)
forward(v)
left(120)
forward(n)

end_fill()



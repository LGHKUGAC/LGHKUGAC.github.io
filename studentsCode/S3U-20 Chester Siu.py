from turtle import *
r = 15
pensize(4)
speed(0)
bgcolor('sandybrown')
for i in range(5):
  fillcolor('lightcoral')
  begin_fill()
  circle(r)
  right(30)
  r = r+3
  end_fill()
for i in range(5):
  fillcolor('brown')
  begin_fill()
  circle(r)
  right(20)
  r = r+3
  end_fill()
for i in range(1):
  fillcolor('firebrick')
  begin_fill()
  circle(r)
  left(5)
  r =r-5
  end_fill()
for i in range(4):
  fillcolor('red')
  begin_fill()
  circle(r)
  left(20)
  r =r-10
  end_fill()

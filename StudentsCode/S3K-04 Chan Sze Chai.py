#paste your code here:

x = 10.5
y = 10
speed(15)
bgcolor('black')
pencolor('black')
fillcolor('white')
begin_fill()
for i in range(5):
  goto(0,-10)
  circle(y)
  y = y*2
  forward(10)
  goto(0,5)
  penup()
  right(100)
  forward(20)
  pendown()
  circle(x*2)
end_fill()

penup()
forward(150)
pendown()


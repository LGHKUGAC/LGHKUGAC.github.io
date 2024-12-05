#paste your code here:

speed(-100)
    
def draw_square(size, colour):
  pencolor(colour)
  for i in range(4):
    forward(size+50)
    left(90)

#1. CUBE
pencolor('white')
pensize(1.5)
bgcolor('black')
fillcolor('darkblue')
begin_fill()
for a in range(4):
  forward(50)
  right(90)
left(20)
forward(33)
right(20)
forward(50)
left(20)
backward(35)
forward(35)
right(110)
forward(50)
right(70)
forward(35)
right(65)
end_fill()
fillcolor('tan')
begin_fill()
goto(0, 0)
right(135)
forward(50)
right(90)
forward(50)
end_fill()

#2. 
bgcolor('darkgreen')
pencolor('gold')
penup()
forward(33)
left(90)
backward(10)
pendown()
bgcolor('black')
  
for s in range(3):
  circle(60+s*10)
  right(90)
  draw_square(s*10, 'darkgreen')
  penup()
  forward(10)
  pendown()
  left(90)

pencolour('purple')
penup()
backward(170)
left(90)
forward(50)
left(90)
pendown()

for y in range(12):
    forward(50)
    right(170)
    forward(50)
    left(140)
    
hideturtle()


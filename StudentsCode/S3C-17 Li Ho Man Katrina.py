#paste your code here:
speed(0)
pensize(4)
bgcolor('black')  
fillcolor('yellow')
  
def draw_shape(colour): #draw shape (star)
  pendown()
  begin_fill()
  pencolor(colour)
  for i in range(5):
    forward(30)
    right(144) 
  end_fill()
penup()
goto(-140,100)
draw_shape('yellow') 

penup()
goto(60, 80)
draw_shape('white') 

penup()
goto(100, 20)
draw_shape('white') 

penup()
goto(-130, 0)
draw_shape('yellow') 

penup()
goto(0,0)
pendown()
outpetals = 11
inpetals = 8
inpetals_angle = 360 / inpetals
outpetals_angle = 360 / outpetals
pensize(4)
pencolor('skyblue')
fillcolour('skyblue')
for i in range(int (outpetals)):
  begin_fill()
  for i in range (2) :
    forward (60)
    left(45)
    forward (60)
    left(135)
  end_fill()
  left (outpetals_angle)
pencolor('white')
fillcolour('white')
for i in range (int(inpetals)): #using loops
  begin_fill()
  for i in range (4) :
    forward (50)
    left(90)
  end_fill()
  left(inpetals_angle)
  
penup()
goto(0,-50)
pendown()
pencolor('blue')
r = 10
x = 5

for i in range(x):
  circle(r)
  r = r + 10
penup()


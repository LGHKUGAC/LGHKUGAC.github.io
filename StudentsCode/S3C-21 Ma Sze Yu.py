#paste your code here:

hideturtle()

speed(0)
bgcolor('black')

for i in range(50):
  r = 77+131*i//50
  g = 77-38*i//50
  b = 255-207*i//50
  col =(r,g,b)
  color(col)
  pensize(4)
  penup()
  goto(0,-50+i)
  pendown()
  begin_fill()
  circle(50-i)
  end_fill()

pensize(5)
fillcolor('white')

sides = 8

angle = 360/sides
            
begin_fill()
            
def draw_shape(colour):
  pencolor(colour)
  for i in range(2):
    forward(10)
    left(50)
    forward(10)
    left(130)

for i in range(sides):
  draw_shape('white')
  left(angle)
  
end_fill()




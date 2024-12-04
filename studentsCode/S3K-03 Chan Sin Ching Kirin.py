#paste your code here:

speed(8)
penup()
goto(-25,-100)
pendown()

fillcolor('white')

for i in range(6):
  begin_fill()
  pencolor('white')
  forward(50)
  pencolor('red')
  left(30)
  circle(50)
  pencolor('white')
  forward(50)
  pencolor('forestgreen')
  left(30)
  circle(50)
  end_fill()

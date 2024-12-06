#paste your code here:
speed(0)
pensize(4)
bgcolor('black')
fillcolor('pink')
sides = 7
begin_fill()
for i in range(sides):
  pencolor('white')
  circle(30)
  left(360/sides)
  goto(0,0)
end_fill()  
pencolor('yellow')
pensize(5)
for i in range(sides):  
  forward(20)
  goto(0,0)
  left(360/sides)
#comments A flower is formed by using loops of circles and lines as the petals and stamens respectively.  


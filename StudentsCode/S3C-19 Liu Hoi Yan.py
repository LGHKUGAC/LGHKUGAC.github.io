#paste your code here:

speed(9)

#function for drawing petals
def draw_petal(color):
  pencolor(color)
  for i in range (10):
      forward(50)
      left(108)
      
pensize(3)
bgcolor('black')

#drawig petals with different color
fillcolor('plum')
begin_fill()
draw_petal('orchid')
right(120)
end_fill()

fillcolor('forestgreen')
begin_fill()
draw_petal('darkgreen')
right(120)
end_fill()

fillcolor('salmon')
begin_fill()
draw_petal('orangered')
right(120)
end_fill()

#drawing a circle outside the petals
fillcolor('lightblue')
begin_fill()
penup()
right(90)
forward(70)
pencolor('white')
pendown()
left(90)
circle(70)
left(30)

#for loop for drawing a hexagon
for i in range (6):
  forward(70)
  left(60)




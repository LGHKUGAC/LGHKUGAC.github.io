from turtle import *#for open day
speed(0)
bgcolor('black')
def draw_star(x, y, length, color):
  pu()
  goto(x, y)
  pd()
  fillcolor(color)
  pencolor(color)
  pensize(3)
  angle1 = 180-108
  angle2 = 180-36
  begin_fill()
  for k in range(5):
    fd(length)
    lt(angle1)
    fd(length+20)
    rt(angle2)
  end_fill()

def star_line(x, y, colors, number):
    for i in range(number):
        color = colors[i % len(colors)]
        draw_star(x, y, 100*0.9**i, color)
        x += 6
        y -= 2
  
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'white', 'pink']
star_line(-130, 30, colors, 14)
pu()
goto(-140, -100)
pencolor('white')
pensize(8)
pd()
goto(-100, -50)
rt(90)
fd(30)
goto(140, -25)    

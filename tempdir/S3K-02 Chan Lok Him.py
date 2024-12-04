from turtle import *

def major(k):
  penup()
  right(k*60)
  if k == -1:
    forward(25)
    left(60)
  if k == 1:
    forward(25)
  pendown()
  begin_fill()
  right(k*60)
  forward(150)
  left(k*120)
  forward(20)
  left(k*60)
  forward(175)
  right(k*60)
  forward(25)
  right(k*120)
  forward(205)
  right(k*60)
  forward(70)
  right(k*120)
  goto(0, 55)
  end_fill()
  
def square():    
  begin_fill()
  left(60)
  forward(25)
  right(120)
  forward(25)
  right(60)
  forward(25)
  right(120)
  forward(25)
  end_fill()

speed(60)

a1 = random.randint(80, 255)
a2 = random.randint(100, 255)
a3 = random.randint(80, 255)
a4 = random.randint(80, 255)
a5 = random.randint(80, 255)
a6 = random.randint(80, 255)

#pencolor(249,158,76)
pencolor(a1, a2, a3)
pensize(5)
goto(-200,-150)
for k in range(100):

  forward(400)
  goto(-200,-150+3*k)
  #pencolor(249,158-k,76)
  pencolor(a1, a2 - k, a3)
  
  
pencolor('black')
pensize(2)

#fillcolor(248, 208, 130)
fillcolor(a4, a5, a6)

penup()
goto(0,80)
pendown()
right(90)
square()




major(1)
major(-1)

penup()
goto(22.5* 3**0.5,102.5)
pendown()
square()

penup()
goto(-22.5* 3**0.5,102.5)
right(120)
pendown()
square()

penup()
goto(10* 3**0.5, 115)
pendown()
begin_fill()
left(60)
goto(10* 3**0.5,70.5)
goto(12.5* 3**0.5,67.5)
goto(12.5* 3**0.5,-82.5)
goto(22.5* 3**0.5, -72.5)
goto(22.5* 3**0.5, 102.5)
end_fill()

penup()
goto(-10* 3**0.5, 115)
pendown()
begin_fill()
right(60)
goto(-10* 3**0.5,70.5)
goto(-12.5* 3**0.5,67.5)
goto(-12.5* 3**0.5,-82.5)
goto(-22.5* 3**0.5, -72.5)
goto(-22.5* 3**0.5, 102.5)
end_fill()

from turtle import *
bgcolor('black')
speed(0)
penup()
goto(-80,80)
pendown()
pencolor('red')

def cir():
  begin_fill()
  fillcolor('white')
  circle(7)
  end_fill()

def upperbody():
  begin_fill()
  fillcolor('red')
  forward(150)
  left(90)
  circle(75,180)
  end_fill()
  
  penup()
  goto(-46, 120)
  pendown()
  cir()#left eye
  penup()
  goto(24, 120)
  pendown()
  cir()#right eye
  
  penup()
  goto(-40, 140)
  pendown()
  pensize(4)
  right(140)
  forward(50)#left ear
  penup()
  goto(34, 144)
  pendown()
  right(80)
  forward(46)#right ear
  
def middlebody():
  begin_fill()
  fillcolor('red')
  pensize(1)
  right(141)
  forward(100)
  
  circle(12,100)
  right(9.5)
  forward(127)
  
  for i in range(20):
    forward(1)
    left(5)
  right(9.5)
  forward(100)
  end_fill()

def hand():
  begin_fill()
  fillcolor('red')
  for i in range(45):
    right(4)
    forward(1)
  forward(70)
  for i in range(45):
    right(4)
    forward(1)
  forward(70)
  end_fill()
  
def leg():
  begin_fill()
  fillcolor('red')
  right(91)
  forward(30)
  right(90)
  forward(50)
  
  for i in range(45):
    right(4)
    forward(1)
    
  end_fill()

upperbody()
penup()
goto(-80, 68)
pendown()
middlebody()
penup()
goto(80, 68)
pendown()
hand()
penup()
goto(-124, 70)
pendown()
hand()
penup()
goto(-50, -50)
pendown()
leg()
penup()
goto(14, -50)
pendown()
left(1.7)
leg()
hideturtle()
#issue fixed wahahhahahaahhhahaahhahahahhahaahahha
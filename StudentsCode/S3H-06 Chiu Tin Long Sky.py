#paste your code here:
speed(10)
bgcolor('black')
pencolor('orange')
pensize(7)
penup()
backward(150)
right(90)
forward(80)
left(90)
pendown()
fillcolor('gold') 
begin_fill()
def draw(rad):
  for i in range(2):
    circle(rad,90)
    circle(rad//2,90)
seth(-45)
draw(200)
penup()
goto(150, 80)
pendown()
left(180)
def draw(rad):
  for i in range(2):
    circle(rad,90)
    circle(rad//1.9,90)
draw(230)
end_fill()
penup()
left(90)
forward(10)
right(45)
forward(280)
left(150)
pendown()
fillcolor('royalblue') 
begin_fill()
def draw(rad):
  for i in range(2):
    circle(rad,90)
    circle(rad//36,90)
seth(-45)
draw(175)
penup()
left(45)
forward(30)
right(45)
pendown()
def draw(rad):
  for i in range(2):
    circle(rad,90)
    circle(rad//36,90)
seth(-45)
draw(135)
end_fill()
penup()
goto(-5,-135)
pendown()
fillcolor('red') 
begin_fill()
def draw(rad):
  for i in range(2):
    circle(rad//30,90)
    circle(rad,90)
seth(-45)
draw(180)
penup()
goto(-4,-100)
pendown()
def draw(rad):
  for i in range(2):
    circle(rad//30,90)
    circle(rad,90)
seth(-45)
draw(130)
end_fill()



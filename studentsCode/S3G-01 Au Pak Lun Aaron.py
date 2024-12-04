from turtle import *

speed(100)
outpetals = random.randint(3,9) 
inpetals = random.randint(3,9) 
outcolour = random.choice(['red', 'green', 'blue'])
incolour = random.choice(['red', 'green', 'blue'])
inpetals_angle = 360 /inpetals 
outpetals_angle = 360 / outpetals
pensize (4)
pencolor (outcolour)
fillcolour (outcolour)
for i in range(int(outpetals)): 
  begin_fill()
  for i in range(2):
    forward(60)
    left(45)
    forward(60)
    left(135)
  end_fill()
  left(outpetals_angle)
pencolor(incolour)
fillcolour(incolour)
for i in range(int(inpetals)): 
  begin_fill()
  for i in range(4):
    forward (50)
    left(90)
  end_fill()
  left(inpetals_angle)

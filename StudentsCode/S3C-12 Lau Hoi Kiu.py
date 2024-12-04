from turtle import *
def backwards(text):
  backwards_text = ''
  for c in text:
    backwards_text = f'{c}{backwards_text}'
  return backwards_text

#let users to know that I will be drawing the dangerus sign and lead them to press enter
#use backward to make things more sus and attract people to press in
print(backwards('*retne* GOOOO see the DANGEROUS SIGN '))
speed(0)
bgcolor("gold")

#create the background by filling yellow in
penup()
goto(0, -225)
pendown()

#draw a big black circle for the second layer
color("black")
begin_fill()
circle(225)
end_fill()

#draw three triangles in the big circle
penup()
goto(0, 0)
pendown()
color("gold")
begin_fill()
for i in range(3):
    right(120)
    for i in range(3):
        forward(200)
        right(120)
end_fill()
#done frawing the dangerous sign (it is supposed to be oversize)

#draw a little exclaimation mark to show it is a urgent and harmful sign when people see it in places like labs or science related workplace
pendown()
color("red")
begin_fill()
left(100)
forward(120)
right(100)
forward(50)
right(100)
forward(120)
right(80)
forward(10)
end_fill()
penup()
pendown
left(80)
forward(20)
begin_fill()
circle(10)
end_fill()
hideturtle()
#done for everything, thanks for seeing this :)
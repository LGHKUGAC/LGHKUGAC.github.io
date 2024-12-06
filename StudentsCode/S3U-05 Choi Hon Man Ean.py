#paste your code here:
from turtle import *

def first():
    pages = 32
    if pages == 14 or pages < 9:
        print('Error...')
        return

    bgcolor('lightseagreen')
    pencolor('azure')
    pensize(5)
    speed(0)
    def page():
      right(45)
      angle = 360 / pages
      angle2 = 45
      penup()
      goto(0, 0)
      pendown()
      right(angle)
      forward(50)
      right(angle2)
      forward(50)
      goto(0, 0)
    for i in range(pages):
      page()  
first()


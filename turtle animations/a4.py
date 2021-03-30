import turtle
import random
from turtle import Turtle, Screen
color = ['green', 'black', 'yellow', 'red']
screen = Screen()
a = Turtle('turtle')
a.color(random.choice(color), random.choice(color))
a.width(5)
a.speed(-1)
def up():
    a.setheading(90)
    a.forward(90)
def down():
    a.setheading(270)
    a.forward(90)
    
def right():
    a.setheading(0)
    a.forward(90)
   
def left():
    a.setheading(180)
    a.forward(90)
    
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')
def drag(x, y):
    a.ondrag(None)
    a.setheading(a.towards(x, y))
    a.goto(x, y)
    a.ondrag(drag)
    
  

def cr():
    a.clear()
   

def main():
    turtle.listen()
    a.ondrag(drag)
    
    turtle.onscreenclick(cr(), 3)

    screen.mainloop()

main()

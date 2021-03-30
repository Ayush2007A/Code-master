import turtle
import random
a = turtle.Turtle()
a.shape('square')
a.color('green', 'red')
a.speed(2)
a.width(5)

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


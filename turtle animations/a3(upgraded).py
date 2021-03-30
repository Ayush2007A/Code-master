import turtle
import random
color = ['red', 'blue', 'yellow', 'green']
a = turtle.Turtle()
a.shape('turtle')
a.color(random.choice(color), random.choice(color))
b = turtle.Turtle()
b.shape('turtle')
b.color(random.choice(color), random.choice(color))
a.speed(1)
b.speed(0)
a.width(5)
b.width(2)
def up():
    a.setheading(90)
    a.forward(90)
    b.setheading(90)
    b.forward(90)
def down():
    a.setheading(270)
    a.forward(90)
    b.setheading(270)
    b.forward(90)
def right():
    a.setheading(0)
    a.forward(90)
    b.setheading(0)
    b.forward(90)
def left():
    a.setheading(180)
    a.forward(90)
    b.setheading(180)
    b.forward(90)
turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')



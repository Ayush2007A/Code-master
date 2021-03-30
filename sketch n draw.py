import turtle
from turtle import Turtle, Screen
a = turtle.Turtle()
screen = Screen()
a.shape('turtle')
print('Welcome to sketch n draw')
print('select your color 1 and 2')
color_1 = (input('color 1: '))
color_2 = (input('color 2: '))
print('ok! your colors are ' + color_1 + (' and ') + color_2)
print("changed pad's color according to the requirments")
a.color(color_1, color_2)
print('So now you can proceed to draw')
while 1 == 1:
    x = (input('enter command: '))
    if x == ('For()'):
        y = int(input('enter the distance: '))
        a.forward(y)
    if x == ('size-pen()'):
        z = int(input('enter new pensize: '))
        a.pensize(z)
    if x == ('Bac()'):
        o = int(input('select distance: '))
        a.backward(o)
    if x == ('dir;dig()'):
        ol = int(input('enter degrees: '))
        olv = input('enter direction: ')
        if olv == ('right'):
            a.right(ol)
        if olv == ('left'):
            a.left(ol)
    if x == ('set-cor()'):
        color_1 = (input('color 1: '))
        color_2 = (input('color 2: '))
        a.color(color_1, color_2)
    if x == ('"'):
        import sys
        sys.exit()
    if x == ('on-mouse'):
        print('sketch with mouse enabled, now you can not use any other function')
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

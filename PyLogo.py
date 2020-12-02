import turtle
t = turtle.Turtle()
t.shape('turtle')
t.right(270)
def color(color):
    '''changes the color accoriding to the request'''
    t.color(color)
def pencolor(color):
    '''changes the color accoriding to the request'''
    t.pencolor(color)
def fdr(distance):
    '''**args**'''
    t.forward(distance)
def bkd(distance):
    '''**args**'''
    t.backward(distance)
def rt(angle):
    '''turns right according to  the angle entered'''
    t.right(angle)
def lt(angle):
    '''turns right according to  the angle entered'''
    t.left(angle)
def cls():
    '''clears the  whole screen'''
    t.screen.clear()
def ntcls():
    '''clears the screen but will not do anything with turtle'''
    t.clear()
def uppen():
    t.penup()
def pendown():
    t.pendown()
def square(length_of_side):
    '''creates a square'''
    for i in range(4):
        t.forward(length_of_side)
        t.right(90)
        
        

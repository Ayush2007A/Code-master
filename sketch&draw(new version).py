from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Sketch & Draw(2.1.0)")
import turtle
t = turtle.Turtle()
entry = Entry(root, width = 20)
entry.place(x = 0, y = 0)
def ford():
    if entry.get() == ("for"):
        t.forward(100)
    if entry.get() == ("bac"):
        t.backward(100)
    
b = Button(root, text = "Run", command = ford)
b.place(x=150, y=0)

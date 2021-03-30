from tkinter import *
import pywhatkit as py
from PIL import Image, ImageTk
window = Tk()
window.geometry("1000x1000")
window.title('Online Space Club')
fn = StringVar()
entry1 = Entry(window)
entry1.place(x = 280, y = 242)
def a():
    if entry1.get() == ("hi"):
        print("hi")
    else:
        print("bye")

button = Button(window, text="Enter", command=a)
button.pack()

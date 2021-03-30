from tkinter import *
import pywhatkit as py
from PIL import Image, ImageTk
window = Tk()
window.geometry("500x500")
window.title('Online Space Club')
image = Image.open("C:/Users/Ayush/Desktop/tkinter/space.jpg")
photo = ImageTk.PhotoImage(image)
Lab = Label(image = photo)
Lab.pack()
fn = StringVar()
fu = StringVar()
fc = StringVar()
ff = StringVar()
def printt():
    label4 = Label(window, text = "Done!",bg = "brown", fg = "white",  width = 12, font = ("arial"))
    label4.place(x = 150, y = 450)
    try:
        py.sendwhatmsg("+918595899937", "I want to join club", (int(x)), (int(y))  )
    except:
        print('could not register')

        
def exit1():
    exit()

label1 = Label(window, text = "Registeration form", relief = "solid", width = 15, font = ("arial",35,"bold"), fg = "red", bg = "blue")
label1.place(x = 32, y = 53)
label2 = Label(window, text = "First name: ",  width = 15, font = ("arial"))
label2.place(x = 80, y = 240)
entry1 = Entry(window,textvar = fn)
entry1.place(x = 280, y = 242)
label3 = Label(window, text = "Last name:",  width = 15, font = ("arial"))
label3.place(x = 80, y = 280)
entry2 = Entry(window,textvar = fu)
entry2.place(x = 280, y = 282)
b1 = Button(window, text = "login", width = 12, bg = "brown", fg = "white", command = printt)
b1.place(x = 150, y = 450)
b1 = Button(window, text = "Quit", width = 12, bg = "brown", fg = "white", command = exit1)
b1.place(x = 280, y = 450)
label3 = Label(window, text = "Whatsapp number:",  width = 15, font = ("arial"))
label3.place(x = 80, y = 320)
entry2 = Entry(window,textvar = fc)
entry2.place(x = 280, y = 322)
label3 = Label(window, text = "Country Code:",  width = 15, font = ("arial"))
label3.place(x = 80, y = 360)
entry2 = Entry(window,textvar = ff)
entry2.place(x = 280, y = 362)
print("enter time press enter and then fill the form but only run the application in idle and time should be in 24 hours format")
x = input('enter hours when you want to send registration messages ')
y = input('enter minutes ')


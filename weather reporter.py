# python3 -- Weather Application using API 

# importing the libraries 
from tkinter import *
import requests 
import json 
import datetime 
from PIL import ImageTk, Image 


# necessary details 
root = Tk() 
root.title("Weather App") 
root.geometry("450x500") 
root['background'] = "white"

# Image 
# Dates 
dt = datetime.datetime.now() 
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15)) 
date.place(x=5, y=130) 
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15)) 
month.place(x=100, y=130) 

# Time 
hour = Label(root, text=dt.strftime('%I : %M %p'), 
			bg='white', font=("bold", 15)) 
hour.place(x=10, y=160) 
city_name = StringVar() 
city_entry = Entry(root, textvariable=city_name, width=45) 
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S) 




# Search Bar and Button 
city_nameButton = Button(root, text="Search", command=city_name) 
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S) 


# Country Names and Coordinates 
lable_citi = Label(root, text="...", width=0, 
				bg='white', font=("bold", 15)) 
lable_citi.place(x=10, y=63) 

lable_country = Label(root, text="...", width=0, 
					bg='white', font=("bold", 15)) 
lable_country.place(x=135, y=63) 

lable_lon = Label(root, text="...", width=0, 
				bg='white', font=("Helvetica", 15)) 
lable_lon.place(x=25, y=95) 
lable_lat = Label(root, text="...", width=0, 
				bg='white', font=("Helvetica", 15)) 
lable_lat.place(x=95, y=95) 

# Current Temperature 

lable_temp = Label(root, text="...", width=0, bg='white', 
				font=("Helvetica", 110), fg='black') 
lable_temp.place(x=18, y=220) 

# Other temperature details 

humi = Label(root, text="Humidity: ", width=0, 
			bg='white', font=("bold", 15)) 
humi.place(x=3, y=400) 

lable_humidity = Label(root, text="...", width=0, 
					bg='white', font=("bold", 15)) 
lable_humidity.place(x=107, y=400) 


maxi = Label(root, text="Max. Temp.: ", width=0, 
			bg='white', font=("bold", 15)) 
maxi.place(x=3, y=430) 

max_temp = Label(root, text="...", width=0, 
				bg='white', font=("bold", 15)) 
max_temp.place(x=128, y=430) 


mini = Label(root, text="Min. Temp.: ", width=0, 
			bg='white', font=("bold", 15)) 
mini.place(x=3, y=460) 

min_temp = Label(root, text="...", width=0, 
				bg='white', font=("bold", 15)) 
min_temp.place(x=128, y=460) 


# Note 
note = Label(root, text="All temperatures in degree celsius", 
			bg='white', font=("italic", 10)) 
note.place(x=95, y=495) 


root.mainloop() 


	# print following values 
print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 


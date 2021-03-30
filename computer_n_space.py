# Python program to explain os.mkdir() method 

# importing os module 
import os 
from os import environ
# Directory 
directory = "GeeksforGeeks2"

# Parent Directory path 
parent_dir = "C:/Users/"+str(environ.get('user'))+"/OneDrive/Desktop"

# Path 
path = os.path.join(parent_dir, directory) 

# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 
print("Directory '% s' created" % directory) 

# Directory 
directory = "Geeks"

# Parent Directory path 
parent_dir = "C:/Users/moghe/OneDrive/Desktop"

# mode 
mode = 0o666

# Path 
path = os.path.join(parent_dir, directory) 

# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# with mode 0o666 
os.mkdir(path, mode) 
print("Directory '% s' created" % directory) 

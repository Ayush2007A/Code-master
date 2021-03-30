# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:34:45 2020

@author: moghe
"""

from gtts import gTTS 
import os 

# The text that you want to convert to audio 
mytext = input('enter the text: ')

# Language in which you want to convert 
language = input('enter the language code(iso 639-1 language code): ')

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("welcome.mp3") 

# Playing the converted file 
os.system("start welcome.mp3") 

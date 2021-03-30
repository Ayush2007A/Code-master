# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:50:07 2020

@author: moghe
"""
wh = "what is"
import wikipedia
import bs4
import pyttsx3
def info(texlts):
    print(wikipedia.summary(texlts))
def speak(texlt):
    a = pyttsx3.init()
    a.say(texlt)
    a.runAndWait()
def mic():
   import speech_recognition as sr
   recognizer = sr.Recognizer()
   ''' recording the sound '''
   with sr.Microphone() as source:
       print("Adjusting noise ")
       recognizer.adjust_for_ambient_noise(source, duration=1)
       print("recording...")
       cmd = recognizer.listen(source)
       print("Done recording")
       ''' Recorgnizing the Audio '''
       print("Recognizing the text")
       try:
           text = recognizer.recognize_google(
        cmd, 
        language="en-IN"
        )
           print(": {}".format(text))
       except:
        print('pls repeat...')
       if wh in text:
           info(text)        
           
    
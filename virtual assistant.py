# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:38:41 2020

@author: moghe
"""
global wh
wh = "what is"
import wikipedia
import pyttsx3
def speak(r):
    e = pyttsx3.init()
    e.say(r)
    e.runAndWait()
def wk(w):
    speak(wikipedia.summary(w))
def mic():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
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
           wh = "what is"
           if text == ('hello'):
               speak('hi')
       except:
        print('pls repeat...')
    if wh in text:
        wk(text)
    if text == ('bye'):
        speak('good bye')
    if text == ('how are you'):
        speak('good')
    if text == ('where is your home'):
        speak('in super')
    
while True:
    mic_=None
    mic_=mic()
    mic_
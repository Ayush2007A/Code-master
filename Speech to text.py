# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:27:47 2020

@author: moghe
"""
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
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
        cmd, 
        language="hi-IN"
            
        )
        print("Decoded Text : {}".format(text))
    except Exception as ex:
       print(ex)
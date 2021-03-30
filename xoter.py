# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:24:22 2021

@author: moghe
"""
wh = 'what'
yn='your name'
def info(ss):
    import wikipedia
    print(wikipedia.summary(ss))
def spk(texta_):
    import pyttsx3
    e=pyttsx3.init()
    e.say(texta_)
    e.runAndWait()
def highermic():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0)
        print("Listning...")
        cmdcs = recognizer.listen(source)
        print("Done recording")
        try:
            global text
            text = ""
            text = recognizer.recognize_google(
        cmdcs, 
        language="en-IN"
            
        )
            global cmd
            cmd = text
            print("{}".format(text))
        except Exception as ex:
            print(ex)
    cmd = text
def check():
    if wh in cmd:
        try:
            if wh and yn in cmd:
                spk('xoter')
            else:
                info(cmd)
        except:
            info(cmd)
def lowermic():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0)
        print("Sleeping....")
        cmdcs = recognizer.listen(source)
        try:
            global text
            text = ""
            text = recognizer.recognize_google(
        cmdcs, 
        language="en-IN"
            
        )
            global cmd
            cmd = text
            print("{}".format(text))
        except Exception as ex:
            print(ex)
    cmd = text
    if cmd == 'xoter':
        highermic()
    else:
        None
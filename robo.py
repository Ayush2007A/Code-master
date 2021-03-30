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
def main():
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
    if wh in cmd:
        wor = cmd
        wor.replace('what ','')
        info(wor)
    if wh and yn in cmd:
        spk('robo')
    if cmd == 'hello':
        spk('hello')
while True:
    try:
        main()
    except:
        print('can not understand your words please speak again.....')
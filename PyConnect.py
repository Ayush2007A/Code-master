# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:15:00 2020

@author: moghe
"""
import time
import webbrowser as web
import pyautogui
import smtplib
import pyperclip as p
import speech_recognition as sr
import translate
def translate(from_language,to_language,Text):
    '''will translate several languages'''
    from translate import Translator
    translator= Translator(from_lang=from_language ,to_lang=to_language)
    translation = translator.translate(Text)
    print (translation)
def onmic():
    print('mic is on')
def speech_to_text(translation_language):
    '''will convert speech to text'''
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("recording...")
        cmd = recognizer.listen(source)
        print("Done recording")
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
        cmd, 
        language=translation_language
            
        )
        print("Text : {}".format(text))
    except Exception as ex:
        print(ex)
def copy(text):
    p.copy(text)
def paste():
    p.paste()
def sendmail(my_mail, my_password, mail_to, content):
    x = input('have you enabled less secure apps in your gmail? y/n: ')
    if x == ('y'):
        print('please wait')
    else:
        print('you can not use this attribute first enable less secure apps on:\n\n https://accounts.google.com/ServiceLogin?service=accountsettings&passive=1209600&osid=1&continue=https://myaccount.google.com/lesssecureapps&followup=https://myaccount.google.com/lesssecureapps&emr=1&mrp=security&rart=ANgoxcfJqycagXbKQsOorlkHJMghNnG94hOIwcpdWOZC28i6v6FBsJHZS9pvja67cREkbq1sxVhhKSBkF3yckUDGNDire8BZkg&authuser=0')
        raise Exception
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(my_mail, my_password) # eneter your email and password but you have to enable <less secure app> in your email privacy setting
    server.sendmail(my_mail, mail_to, content) # eneter your email, reciver email, content to send
    server.close()
    print('sent your mail')
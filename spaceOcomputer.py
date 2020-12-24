# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 20:12:30 2020

@author: moghe
"""
# importing modules
import pyttsx3
en=pyttsx3.init()
import wikipedia
import ephem
import datetime
from datetime import datetime, timedelta
import numpy as _np
from scipy import constants
import os
def date_solar_eclipse():
    '''will give predecting details for solar eclipses'''
    import ephem
    from datetime import datetime, timedelta
    curtime = datetime(2001, 1, 1, 0, 0, 0)        # start time
    endtime = datetime(2100, 12, 31, 23, 59, 59)   # end time
    moon = ephem.Moon()
    sun = ephem.Sun()
    observer = ephem.Observer()
    observer.elevation = -6371000    # place observer in the center of the Earth
    observer.pressure = 0            # disable refraction
    while curtime <= endtime:
         observer.date = curtime.strftime('%Y/%m/%d %H:%M:%S')
         # computer the position of the sun and the moon with respect to the observer
         moon.compute(observer)
         sun.compute(observer)
         # calculate separation between the moon and the sun, convert
         # it from radians to degrees
         sep = abs((float(ephem.separation(moon, sun))
                    / 0.01745329252))
         # a solar eclipse happens if Sun-Earth-Moon alignment is <1.5976°.
         # this should detect all total and partial eclipses, but will
         # include some near misses.
         if sep < 1.59754941:
             print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)
             # an eclipse cannot happen more than once in a day,
             # so we skip 24 hours when an eclipse is found
             curtime += timedelta(days = 1)
         else:
            # advance five minutes if an eclipse is not found
            curtime += timedelta(minutes = 5)
def date_lunar_eclipse():
    '''will give predicting details for lunar eclipses'''
    currenttime = datetime(2001,1,1,0,0,0)
    endtime=datetime(2100,12,31,23,59,59)
    moon=ephem.Moon()
    sun=ephem.Sun()
    observer=ephem.Observer()
    observer.elevation= -6371000
    observer.pressure = 0
    while currenttime <= endtime:
        observer.date=currenttime
        moon.compute(observer)
        sun.compute(observer)
        sep = abs((float(ephem.separation(moon, sun))
                   / 0.01745329252) - 180)
        if sep < 0.9:
            print(currenttime.strftime('%Y/%m/%d %H:%M:%S'), sep)
            currenttime += timedelta(days = 1)
        else:
            currenttime += timedelta(hours = 1)
def visibility_planet(planet1,planet2,date_):
    '''will give details about planetary visibility or seperation'''
    p1 = ephem.Mars()
    p2 = ephem.Venus()
    p3 = ephem.Jupiter()
    p4 = ephem.Saturn()
    p5 = ephem.Moon()
    p6 = ephem.Mercury()
    p7 = ephem.Uranus()
    observer= ephem.Observer()
    observer.date = ephem.date(date_)
    if planet1 == 'mars':planet1= ephem.Mars()
    if planet1 =='venus':planet1= ephem.Venus()
    if planet1 == 'jupiter':planet1= ephem.Jupiter()
    if planet1 == 'saturn':planet1= ephem.Saturn()
    if planet1 == 'mercury': planet1 =  ephem.Mercury()
    if planet1 == 'uranus': planet1 =  ephem.Uranus()
    if planet2 == 'mars':planet2=ephem.Mars()
    if planet2 =='venus':planet2=ephem.Venus()
    if planet2 == 'jupiter':planet2= ephem.Jupiter()
    if planet2 == 'saturn':planet2=ephem.Saturn()
    if planet2 == 'mercury': planet2 =ephem.Mercury()
    if planet2 == 'uranus': planet2 =  ephem.Uranus()
    planet1.compute(observer)
    planet2.compute(observer)
    print(ephem.separation(planet1,planet2))
def knowledge(question):
    print(wikipedia.summary(question))
def start(what_to_start):
    '''will start the required'''
    os.system('start '+what_to_start)
def speak(scentence):
    '''will speak the required'''
    en.say(scentence)
    en.runAndWait()
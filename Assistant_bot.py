# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:26:08 2021

@author: moghe
"""
hito=['hello','hi','yo','hey']
hi='hi'
hn='hello'
wh='what'
hw='how'
strt='start'
# import module 
import random
import os
import requests 
import bs4 
import PanclusGz
from PanclusGz import Gz as gz

def searchon(searcher,url_to_search):
    # Taking thecity name as an input from the user 
    search = searcher
    # Generating the url 
    url = url_to_search + search 
    # Sending HTTP request 
    request_result = requests.get( url ) 
    # Pulling HTTP data from internet 
    soup = bs4.BeautifulSoup( request_result.text ,"html.parser" ) 
    temp = soup.find( "div" , class_='BNeawe' ).text
    print(temp)
def main():
    cmd = input('assist: ')
    if hi in cmd:
        print(random.choice(hito))
    if wh in cmd:
        searchon(cmd, 'https://www.google.com/search?q=')
    if hw in cmd:
        searchon(cmd,'https://www.google.com/search?q=')
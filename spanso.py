# Hi I am Spanso
wh = "what is"
import wikipedia
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello!!")
engine.runAndWait()  
print('Hello, Sir')
def mic():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("recording...")
        cmdcs = recognizer.listen(source)
        print("Done recording")
        try:
            global text
            print("Recognizing the text")
            text = recognizer.recognize_google(
        cmdcs, 
        language="en-IN"
            
        )
            global cmd
            cmd = text
            print("Decoded Text : {}".format(text))
        except Exception as ex:
            print(ex)
    cmd = text
    import pyttsx3
    engine = pyttsx3.init()
    if cmd == ('o'):
        cmd = ""
        engine.say("d")
        engine.runAndWait()            
    if cmd == ('hi'):
        cmd = ""
        engine.say("hi")
        engine.runAndWait()        
    if cmd == ('web'):
        import webbrowser
        new=2;

        url= input("enter the name of web browser or website or link ");

        webbrowser.open(url, new=new);
    if cmd == ('search wiki'):
        import webbrowser

        re = input('enter your search term ')

        new = 2;

        url = ("https://en.wikipedia.org/wiki/");

        webbrowser.open(url + re, new=new)
    if cmd ==('search web'):
        import webbrowser

        re = input('enter your search term ')

        new = 2;

        url = ("https://www.google.com/search?q=");

        webbrowser.open(url + re, new=new)
    if cmd == ('math'):
        calculate = input("type one to add, two to subtract, three to multiply and four to divide ")
        if calculate == ('one'):
            print('select two numbers')
            no_1 = (int(input('number one ')))
            no_2 = (int(input('number two ')))
            print(no_1 + no_2)

        if calculate == ('two'):
            print('select two numbers')
            no_1 = (int(input('number one ')))
            no_2 = (int(input('number two ')))
            print(no_1 - no_2)

        if calculate == ('three'):
            print('select two numbers')
            no_1 = (int(input('number one ')))
            no_2 = (int(input('number two ')))
            print(no_1 * no_2)

        if calculate == ('four'):
            print('select two numbers')
            no_1 = (int(input('number one ')))
            no_2 = (int(input('number two ')))
            print(no_1 / no_2)


    if cmd == ('you are useless'):
        engine.say("ok, if i am useless, then bye")
        engine.runAndWait()
        import sys
        sys.exit()
    if cmd == ('show my shopping list'):
        print((str([a + b + c + d])))
    if cmd == ('add item in my shopping list'):
        engine.say("you can add only four items")
        engine.runAndWait()
        a = input('item one ')
        b = input('item two ')
        c = input('item three ')
        d = input('item four ')
        print ('your current shopping list is,' + (str([a + b + c + d])))
    if cmd == ('show date'):
        import datetime
        engine.say(datetime.date.today())
        engine.runAndWait()
    if cmd == ('show time'):
        import time as tm
        time = tm.strftime('%H:%M:%S')
        engine.say(time)
        engine.runAndWait()
    if cmd == ('what is your name'):
        engine.say("Spanso!")
        engine.runAndWait()
    if cmd == ('spanso'):
        engine.say("yes,sir")
        engine.runAndWait()
    if cmd == ('sing a song'):
        import webbrowser

        new = 2;

        url = ("ganna.com");

        webbrowser.open(url, new=new)
    if cmd == ('play game'):
        engine.say("I know some games!")
        engine.runAndWait()
        engine.say("gussing game?")
        engine.runAndWait()
        ans = input('y/n ')
        if ans == ('y'):
            engine.say("ok, here it is")
            engine.runAndWait() 
            print('hi i am thinking of a number from one to six, can you guess it in a four turns?Let us start')
            import random
            x = random.randint(1, 6)
            for i in range(1, 5):
                print('take a guess')
                y = (str(input()))
                if y > (str(x)):
                    print('up')
                elif y < (str(x)):
                    print('down')
                else:
                    break # guess is correct
            if y == (str(x)):
                print('ya the no was ' + (str(x)))
            else:
                print('no, the number was ' + (str(x)))
        if ans == ('n'):
            engine.say("then,repeater")
            engine.runAndWait()
            ans = input('y/n ')
            if ans == ('y'):
                print('hi i am repeater! i will repeat that you will type but you only have 6 chances!!!')
                for i in range(1, 7):
                    print('type any thing, but do not type any number!')
                    ty = input()
                    print(ty)
            if ans == ('n'):
                engine.say("sorry, i don't have more games")
                engine.runAndWait()            
    if cmd == ('play latest bollywood songs'):
        import webbrowser

        new = 2;

        url =("https://www.youtube.com/watch?v=y2WmCzEafGg");

        webbrowser.open(url, new=new)
    if cmd == ('play news'):
        import webbrowser

        new = 2;

        url =("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en");

        webbrowser.open(url, new=new)

    if cmd == ('start skills'):
        engine.say("which skill would you like to enable")
        engine.runAndWait()                
        x = input()
        if x == ('put in value'):
            print('ok, here it is!')
            print('type name of variable')
            c = input()
            print('type the value of variable')
            v = (input())
            print (c + '=' + v)
        if x == ('hanuman chalisa'):
            print('ok, here it is')
            import webbrowser

            new = 2;

            url =("https://www.youtube.com/watch?v=AETFvQonfV8");

            webbrowser.open(url, new=new)    
       
       

        if x == ('morning bhajan'):
            import webbrowser

            new = 2;

            url =("https://www.youtube.com/watch?v=Gjj_oo24Rks");

            webbrowser.open(url, new=new)
    if cmd == ('set alarm'):
        import datetime
        h = (int(input('set hours ')))
        m = (int(input('set minutes ')))
        ap = (str(input('am or pm ')))

        if ap == ('pm'):
            h = h +12

        while 1 == 1:
            if(h == datetime.datetime.now().hour and
               m == datetime.datetime.now().minute):
                engine.say("Time's up, time's up")
                engine.runAndWait()
                break
    if cmd == ('what is my name'):
        cmd = ""
        engine.say("Ayush")
        engine.runAndWait()
    if cmd == ('bye'):
        import sys
        engine.say("bye")
        engine.runAndWait()
        sys.exit()
    if cmd == ('show animation'):
        engine.say("can't do that")
        engine.runAndWait()
    if cmd == ('hello'):
        engine.say("hi  bro")
        engine.runAndWait()
    if cmd == ('show loop'):
        engine.say("really?")
        engine.runAndWait()
        r = input('type yes or no ')
        if r == ('yes'):
            print('ok here is the loop!')
            while 1 == 1:
                print('loop')
                
        if r == ('no'):
            engine.say("ok")
            engine.runAndWait()
    if cmd == ('apply new name'):
        name = input('enter my new name ')
        print('so only for this time my new name is ' + name)
    if cmd == ('your new name'):
        print(name)
    if cmd == ('what is your new name'):
        engine.say(name)
        engine.runAndWait()

    if cmd == ('calculate my percentage'):
        print('enter your marks but you can enter marks of seven subjects only!')
        p = (int(input()))
        q = (int(input()))
        r = (int(input()))
        s = (int(input()))
        t = (int(input()))
        u = (int(input()))
        v = (int(input()))
        print('enter total of max marks')
        tot = (int(input()))
        sutot = (p + q + r + s + t + u + v)
        print ('percentage is')
        print(sutot/tot * 100 )
    if cmd == ('how are you'):
        engine.say("good")
        engine.runAndWait()
    if cmd == ('sing in your voice'):
        engine.say("I can only sing one song, so let us start,  Tuujhe, Dekhaa, to ye jaanaa, sanam, pyaar hotaa deevaanaa sanam, aab kahan, se jayen hum, teri baahon me ghaar jaaye haam.tujhe dekha!   I don't know any more!!")
        engine.runAndWait()
    if wh in cmd:
        engine.say(wikipedia.summary(cmd))
        engine.runAndWait()
#######################################################################################################################################################################################################################################
while True:
    try:
        mic()
    except:
        None
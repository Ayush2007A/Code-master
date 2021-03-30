# Hi I am Spanso
print('Hello, Sir')
for i in range(1, 178283903809374302978379853764837849494738393837272721910100202023937843646467477):
    cmd = input()
    if cmd == ('o'):
            print('o')
    if cmd == ('hi'):
        print ('hi')
    if cmd == ('web'):
        import webbrowser
        new=2;

        url= input("enter the name of web browser or website or link ");

        webbrowser.open(url, new=new);
    if cmd == ('search reasult'):
        import webbrowser

        new = 2

        tabUrl = "https://www.google.com/search?source="

        search = input("Enter search query ");

        webbrowser.open(tabUrl + search, new=new)

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
        print('ok as you wish, if you do not want me, then bye!!')
        import sys
        sys.exit()
    if cmd == ('show my shopping list'):
        print('your shopping list is empty')
    if cmd == ('add item in my shopping list'):
        print('you can add only three items!')
        a = input('item one ')
        b = input('item two ')
        c = input('item three ')
        d = input('item four ')
        print ('your current shopping list is,' + (str([a + b + c + d])))
    if cmd == ('show date'):
        import datetime
        print(datetime.date.today())
    if cmd == ('show time'):
        import time as tm
        time = tm.strftime('%H:%M:%S')
        print (time)
    if cmd == ('what is your name'):
        print('spanso!')
    if cmd == ('spanso'):
        print('yes, sir')
    if cmd == ('sing a song'):
        import webbrowser

        new = 2;

        url = ("ganna.com");

        webbrowser.open(url, new=new)
    if cmd == ('play game'):
        print('I know some games!')
        print('gussing game?')
        ans = input('y/n ')
        if ans == ('y'):
            print('ok')
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
            print('then, repeater?')
            ans = input('y/n ')
            if ans == ('y'):
                print('hi i am repeater! i will repeat that you will type but you only have 6 chances!!!')
                for i in range(1, 7):
                    print('type any thing, but do not type any number!')
                    ty = input()
                    print(ty)
    
        
    
    

        
    

        
            
        

        
            
        
    
    

        

        

        





        
    



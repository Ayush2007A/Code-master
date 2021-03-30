pl = ('+')
c1 = ('[[')
c2 = (']]')
cn1 = ("'")
cn2=("'")
prt = ('show')
cb1 = ('{')
eq = ('=')
while True:
    x= input('Aplha >')
    if cn1 and cn2 in x:
        print(x)
    if c1 in x:
        while True:
            y=input('  ')
            if eq and cb1 in y:
                a=set(input('  \n'))
                print(a)
            elif y == "]]":
                break
        
    

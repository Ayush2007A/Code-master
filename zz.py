# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 08:20:24 2020

@author: moghe
"""
def login():
    speak('Logging...')
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    with sr.Microphone() as source:
        speak('please speak your name')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listning...")
        cmdcst = recognizer.listen(source)
        print("Logging....")
        try:
            global text
            text = ""
            speak('performing final login!')
            textn = recognizer.recognize_google(
        cmdcst, 
        language="en-IN"
            
        )
            print("Logged as : {}".format(textn))
            speak('logged as '+ textn)
        except Exception as ex:
            print(ex)
import wikipedia
import pyttsx3
import datetime
import time as tm
import webbrowser
import os
t = 'time'
d = 'date'
strt='start'
wh = 'what'
hw = 'how'
shu='shutdown'
lst = 'listen'
solar='solar eclipse'
lunar = 'lunar eclipse'
cn = 'can'
gr = 'great'
gd = 'good morning'
gn = 'good night'
pl = 'plus'
bl = 'belong'
yrn = 'your name'
plus = '+'
minus = '-'
plt='Play'
pltst='play'
ts = 'tell'
ab = 'about'
lv = 'live'
who='who'
mn='my name'
sc = 'song'
scs = 'songs'
why = 'why'
whi = 'which'
yr = 'yourself'
span = 'spanso'
sor = 'source code'
def ssc(term):
    new = 2
    url = 'https://www.youtube.com/results?search_query='
    webbrowser.open(url+term,new)
def inf():
    math()
from sly import Lexer
class BasicLexer(Lexer): 
	tokens = { NAME, NUMBER, STRING } 
	ignore = '\t '
	literals = { '=', '+', '-', '/', 
				'*', '(', ')', ',', ';'} 


	# Define tokens as regular expressions 
	# (stored as raw strings) 
	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
	STRING = r'\".*?\"'

	# Number token 
	@_(r'\d+') 
	def NUMBER(self, t): 
		
		# convert it into a python integer 
		t.value = int(t.value) 
		return t 

	# Comment token 
	@_(r'//.*') 
	def COMMENT(self, t): 
		pass

	# Newline token(used only for showing 
	# errors in new line) 
	@_(r'\n+') 
	def newline(self, t): 
		self.lineno = t.value.count('\n')
from sly import Parser
class BasicParser(Parser): 
	#tokens are passed from lexer to parser 
	tokens = BasicLexer.tokens 

	precedence = ( 
		('left', '+', '-'), 
		('left', '*', '/'), 
		('right', 'UMINUS'), 
	) 

	def __init__(self): 
		self.env = { } 

	@_('') 
	def statement(self, p): 
		pass

	@_('var_assign') 
	def statement(self, p): 
		return p.var_assign 

	@_('NAME "=" expr') 
	def var_assign(self, p): 
		return ('var_assign', p.NAME, p.expr) 

	@_('NAME "=" STRING') 
	def var_assign(self, p): 
		return ('var_assign', p.NAME, p.STRING) 

	@_('expr') 
	def statement(self, p): 
		return (p.expr) 

	@_('expr "+" expr') 
	def expr(self, p): 
		return ('add', p.expr0, p.expr1) 

	@_('expr "-" expr') 
	def expr(self, p): 
		return ('sub', p.expr0, p.expr1) 

	@_('expr "*" expr') 
	def expr(self, p): 
		return ('mul', p.expr0, p.expr1) 

	@_('expr "/" expr') 
	def expr(self, p): 
		return ('div', p.expr0, p.expr1) 

	@_('"-" expr %prec UMINUS') 
	def expr(self, p): 
		return p.expr 

	@_('NAME') 
	def expr(self, p): 
		return ('var', p.NAME) 

	@_('NUMBER') 
	def expr(self, p): 
		return ('num', p.NUMBER)
class BasicExecute: 
	
	def __init__(self, tree, env): 
		self.env = env 
		result = self.walkTree(tree) 
		if result is not None and isinstance(result, int): 
			print(result) 
		if isinstance(result, str) and result[0] == '"': 
			print(result) 

	def walkTree(self, node): 

		if isinstance(node, int): 
			return node 
		if isinstance(node, str): 
			return node 

		if node is None: 
			return None

		if node[0] == 'program': 
			if node[1] == None: 
				self.walkTree(node[2]) 
			else: 
				self.walkTree(node[1]) 
				self.walkTree(node[2]) 

		if node[0] == 'num': 
			return node[1] 

		if node[0] == 'str': 
			return node[1] 

		if node[0] == 'add': 
			return self.walkTree(node[1]) + self.walkTree(node[2]) 
		elif node[0] == 'sub': 
			return self.walkTree(node[1]) - self.walkTree(node[2]) 
		elif node[0] == 'mul': 
			return self.walkTree(node[1]) * self.walkTree(node[2]) 
		elif node[0] == 'div': 
			return self.walkTree(node[1]) / self.walkTree(node[2]) 

		if node[0] == 'var_assign': 
			self.env[node[1]] = self.walkTree(node[2]) 
			return node[1] 

		if node[0] == 'var': 
			try: 
				return self.env[node[1]] 
			except LookupError: 
				print("Undefined variable '"+node[1]+"' found!") 
				return 0
if __name__ == '__main__': 
	lexer = BasicLexer() 
	parser = BasicParser() 
	print('''Spanso''') 
	env = {} 
def math(expre):
    try:
        text = expre 
    except EOFError:
        print('???????????????')
		
    if text:
        tree = parser.parse(lexer.tokenize(text))
        BasicExecute(tree, env)
class _if:
    tokens=['if'
            'else'       
        
        ]

def speak(text_):
    e=pyttsx3.init()
    e.setProperty("rate",200)
    e.say(text_)
    e.runAndWait()
def shutdown(time = 0):
    """Will shutdown the computer in given seconds
For Windows and Linux only"""
    global osname
    osname = platform.system()
    if "window" in osname.lower():
        cont = "shutdown -s -t %s"%time
        os.system(cont)

    elif "linux" in osname.lower():
        cont = "shutdown -h %s"%time
        os.system(cont)

    elif "darwin" in osname.lower():
        cont = "shutdown -h -t %s"%time
        os.system(cont)

    else:
        raise Warning("This function is for Windows, Mac and Linux users only, can't execute on %s"%osname)
def info(text):
    speak(wikipedia.summary(text))
def main():
    cmd=input('command> ')
    if wh in cmd:
        info(cmd)
    if hw in cmd:
        info(cmd)
    if plt in cmd:
        speak('playing....')
        import webbrowser
        new=2;
        url='https://www.youtube.com/results?search_query='
        webbrowser.open(url+cmd,new)
    
    if cn in cmd:
        info(cmd)
    if shu in cmd:
        speak('shutting down')
        cont = "shutdown /s /f /t 0"
        os.system(cont)
    if cmd == 'hello':
        speak('hi')
    if plus in cmd:
        pl = '+'
        speak(math(cmd))
    if minus in cmd:
        speak(math(cmd))
    if pltst in cmd:
        speak('playing....')
        import webbrowser
        new=2;
        url='https://www.youtube.com/results?search_query='
        webbrowser.open(url+cmd,new)
        t.sleep(5)
        import pyautogui
        pyautogui.click(x=741, y=255)
    if plt in cmd:
        speak('playing....')
        import webbrowser
        new=2;
        url='https://www.youtube.com/results?search_query='
        webbrowser.open(url+cmd,new)
        t.sleep(5)
        import pyautogui
        pyautogui.click(x=741, y=255)
    if cmd == 'how are you':
        speak('fine how about you')
    if t in cmd:
        time = tm.strftime('%H:%M:%S')
        speak('time is, ' +time)
    if d in cmd:
        speak(datetime.date.today())
    if ab in cmd:
        info(cmd)
    if ts in cmd:
        info(cmd)
    if lv in cmd():
        speak('i live in a  laptop')
    if who in cmd:
        info(cmd)
    if sc in cmd:
        ssc(cmd)
    if scs in cmd:
        ssc(cmd)
    if why in cmd:
        info(cmd)
    if whi in cmd:
        info(cmd)
    if cmd == 'what are you doing':
        speak('MY,job')
    if yr in cmd:
        speak('i am  spanso,my job is to work  with ayush and listen the things that are taught in the class')
    if span in cmd:
        speak('yes,tell')
    if sor in cmd:
        speak('no,i can not')
    if yrn in cmd:
        speak('spanso the great')
    if gr in cmd:
        speak('god knows')
    if bl in cmd:
        speak('i belong from this world')
    if gd in cmd:
        speak('good,morning')
    if gn in cmd:
        speak('good night')
    if lst in cmd:
        speak('speak')
    if strt in cmd:
        os.startfile(cmd)
    if sc in cmd:
        ssc(cmd)
    
login()
while True:
    try:
        main()
    except:
        try:
            main()
        except:
            print('no')
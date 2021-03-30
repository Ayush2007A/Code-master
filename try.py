# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:29:09 2021

@author: moghe
"""
import keyboard
import os
import sys
import signal
from sympy import *
from colorama import Fore, Back, Style
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        t[0] = 0

def p_error(t):
    pass

import ply.yacc as yacc
parser = yacc.yacc()

print('Asst prompt: Your assistant\n')
def keyboardInterruptHandler(signal, frame):
    print(("\nKeyboardInterrupt".format(signal)))
    while True:
        main()
def set_variables(variables):
    return symbols(variables)
signal.signal(signal.SIGINT, keyboardInterruptHandler)

def main():
    code=input('asst--> ')
    parser.parse(code)
    if 'press' in code:
        string = code
        word = 'press'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        try:keyboard.send(out)
        except:print('unable to press key')
    if 'type' in code:
        string = code
        word = 'type'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print(out)
    if 'python install' in code:
        string = code
        word = 'python install'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        print('Installing',out,'using pip')
        import time
        time.sleep(3)
        import pip
        pip.main(['install',out])
        print('successfully installed',out)
    if 'delete' in code:
        string = code
        word = 'delete'
        word_list = string.split()
        out=(' '.join([i for i in word_list if i not in word]))
        import os
        os.system('del '+out)
while True:
    main()

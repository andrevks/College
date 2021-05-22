# -*- coding: utf-8 -*-
"""LexicalAnalyser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vhZMpLs7XgNqR4GfyzaLsNy3FY60npFX

# Lexical Analyser

Owner: André Geraldo 

Course: Computer Enginnering

Steps:

1- Read a file containing a source code with a specific syntax

2 - User a buffer to take each line and classify them 

3 - Regex will recognise if a token is valid and store them

4 - store each token in the the following format:
 [Token, Lexema, Line, Column]
"""

#import of regex
import re

class Lexer:

  def __init__(self, source_code):
    #self.__especiais = ['+','/']
    #self.__buffer = []
    self.__source_code = source_code

  def scanning(self):

    buffer = self.__source_code
    #defining the pattern
    pattern = re.compile(r'funny')


    matches = pattern.finditer(buffer)
 
    print("\nBuffer: ")
    print(buffer)
    print("\n")
    for match in matches:
      print(match)


def main():
  #read the current fun lang file in test.lang
  # and store it in a buffer

  content = ""
  with open("lang.txt", "r") as file:
    content = file.read()

  lex = Lexer(content)
  tokens = lex.scanning()


main()

import re

text_to_search = '''
BeginFun
  funny variable.
  variable <- 10 * (124+ 666).
EndFun

'''

regexRules = '''

'''
pattern = re.compile(r'\d+')

matches = pattern.finditer(text_to_search)

for match in matches:
  print(match)

print(text_to_search[12:17])

subject = "Data Science"
language = "Python"

output_str = "I am studying %s and using Python as the programming language." %subject 

print(output_str)

list1 = [('NUMBER', r'\d+'),( 'ASSIGN',  r':=') ]
list2 = [('NOME_TOKEN', r'REGEX_EXP'),('NOME_TOKEN2', r'REGEX_EXP2') ]
token = "|".join('(?P<%s>%s)' % pair for pair in list1)



print(token)

from typing import NamedTuple
import re


class Token(NamedTuple):
  type: str
  value: str
  line: int
  column: int


def tokenize(code):
  keywords = {'BeginFun','EndFun','if','then','else','elif','end','funLoopWhile','do','endFunLoop',
              'showMeTheCode','grabInput','funny'}
  token_specification = [
    ('TK_NUM', r'\d+'),
    ('TK_ATRIB', r'<-'),
    ('TK_PERIOD', r'\.'),
    ('TK_ID', r'[A-Za-z]([A-Za-z]|\d|_)*'),
    ('TK_STRING', r'^\"([A-Za-z]|\d|\.|%|:| )*\"$'), #String com aspas
    ('TK_OP_AR', r'[-+*\/]'), #Oerações aritmética
    ('TK_OP_RE', r'[=<>]|<>'),#Operação relacional  
    ('TK_BOOL', r'[|&]'),       
    ('TK_OPEN_P', r'\('),
    ('TK_CLOSE_P', r'\)'),
    ('TK_COMMA', r','),
    ('TK_NEW_LINE',r'\n'),
    ('TK_SKIP', r'[\ \t\r]+'),
    ('MISMATCH', r'.'),                
  ]            

  tk_regex_rules = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

  line_num = 1
  line_start = 0
  for mo in re.finditer(tk_regex_rules,code):
    kind = mo.lastgroup
    value = mo.group()
    column = mo.start() - line_start
    #print("LASTGROUP: ", kind)
     #print("\nVALUE: ", mo.group())
    #print("\nCOLLUMN: ", mo.start() - line_start)
    if kind == 'TK_NUM':
      value = int(value)
    elif value in keywords :
      kind = value
    elif kind == 'TK_NEW_LINE':
      line_start = mo.end()
      line_num += 1
      continue
    elif kind == 'TK_SKIP':
      continue
    elif kind == 'MISMATCH':
      raise RuntimeError(f'{value!r} unexpected on line {line_num}')
    yield Token(kind,value, line_num, column)

    
code_source = '''
BeginFun

 if idade < 10 & anoNasc <> 10 then

	funLoopWhile valor_ethereum < valor_bitcoin do

		showMeTheCode investYourMoney.

	endFunLoop.

 end.
 
EndFun
'''
#tokenize(code_source)
for token in tokenize(code_source):
  print(token)

from typing import NamedTuple
import re

class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    print("REGEX: ", tok_regex)
    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        #print("LASTGROUP: ", mo.lastgroup)
        print("\nVALUE: ", mo.group())
        #print("\nCOLLUMN: ", mo.start() - line_start)
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
   IF quantity THEN
        total:=total-price*quantity;
        tax := price * 5;
    ENDIF;
'''
tokenize(statements)
for token in tokenize(statements):
    print("NADA HAVER: ",token)
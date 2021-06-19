from typing import List, Any

from receiveFlags import args
from receiveFlags import source_code
from syntaxAnalyser import SyntaxAnalyser
from lexicalAnalyser import LexicalAnalyser


def fun_compiler():
    tudo = args.tudo
    lt = args.ltokens
    ls = args.lsintatico
    token_list: List[Any] = []
    if tudo:
        token_list = LexicalAnalyser(source_code, True).switch_mode(lt=True)
        syntax = SyntaxAnalyser(token_list, log=True).switch_mode(log=True)
    else:
        token_list = LexicalAnalyser(source_code, lt).switch_mode(lt)
        syntax = SyntaxAnalyser(token_list, ls).switch_mode(ls)

    if syntax:
        print("\nO arquivo foi RECONHECIDO pelo analisador sintático !\n")
    else:
        print("\nQue Pena! O arquivo foi NÃO FOI RECONHECIDO pelo analisador sintático !\n")


fun_compiler()

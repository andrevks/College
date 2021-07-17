from typing import List, Any

from receiveFlags import args
from receiveFlags import source_code
from syntaxAnalyser import SyntaxAnalyser
from lexicalAnalyser import LexicalAnalyser
from semanticAnalyser import SemanticAnalyser
from intermediateCode import IntermediateCode
from finalAssemblyRaspberry import FinalRaspberry


def clone_list(list):
    li_copy = list[:]
    return li_copy


def syntax_result(syntax):
    if syntax:
        print("\nO arquivo foi RECONHECIDO pelo analisador sintático !\n")
    else:
        print("\nQue Pena! O arquivo foi NÃO FOI RECONHECIDO pelo analisador sintático !\n")


def fun_compiler():
    tudo = args.tudo
    lt = args.ltokens
    ls = args.lsintatico
    lse = args.lsemantico
    ts = args.tsimbolos
    token_list: List[Any] = []
    id_list = []
    if tudo:
        token_list = LexicalAnalyser(source_code, True).switch_mode(lt=True)
        token_list_backup = clone_list(token_list)
        syntax = SyntaxAnalyser(token_list, log=True).switch_mode(log=True)
        syntax_result(syntax)
        id_list = SemanticAnalyser(token_list_backup, lse=True, ts=True).switch_mode(lse=True, ts=True)
        print(f'\nid_list: {id_list} ')
        inter_code = IntermediateCode(id_list, token_list_backup).generate_intermediate_code()
        FinalRaspberry(inter_code, id_list)
    else:
        token_list = LexicalAnalyser(source_code, lt).switch_mode(lt)
        token_list_backup = clone_list(token_list)
        syntax = SyntaxAnalyser(token_list, ls).switch_mode(ls)
        syntax_result(syntax)
        id_list = SemanticAnalyser(token_list_backup, lse, ts).switch_mode(lse, ts)
        print(f'\nid_list: {id_list} ')
        inter_code = IntermediateCode(id_list, token_list_backup).generate_intermediate_code()
        FinalRaspberry(inter_code, id_list)


fun_compiler()

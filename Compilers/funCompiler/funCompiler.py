from typing import List, Any

from util.receiveFlags import args
from util.receiveFlags import source_code
from src.syntaxAnalyser import SyntaxAnalyser
from src.lexicalAnalyser import LexicalAnalyser
from src.semanticAnalyser import SemanticAnalyser
from src.intermediateCode import IntermediateCode
from src.finalAssemblyRaspberry import FinalRaspberry


def clone_list(list):
    li_copy = list[:]
    return li_copy


def syntax_result(syntax):
    if syntax:
        print("\nO arquivo foi RECONHECIDO pelo analisador sintático !\n")
        return True
    else:
        print("\nQue Pena! O arquivo foi NÃO FOI RECONHECIDO pelo analisador sintático !\n")
        return False


def fun_compiler():
    tudo = args.tudo
    lt = args.ltokens
    ls = args.lsintatico
    lse = args.lsemantico
    ts = args.tsimbolos
    tci = args.tintermediario
    lci = args.lintermediario
    lgc = args.lgeracao
    token_list: List[Any] = []
    id_list = []

    if tudo:
        token_list = LexicalAnalyser(source_code, True).switch_mode(lt=True)
        token_list_backup = clone_list(token_list)
        syntax = SyntaxAnalyser(token_list, ls=True)
        if syntax_result(syntax):
            id_list = SemanticAnalyser(token_list_backup, lse=True, ts=True).verify_semantic()
            inter_code = IntermediateCode(id_list, token_list_backup, tci=True, lci=True).generate_intermediate_code()
            final_code = FinalRaspberry(inter_code, id_list, lgc=True).generate_final_code()
    else:
        token_list = LexicalAnalyser(source_code, lt).switch_mode(lt)
        token_list_backup = clone_list(token_list)
        syntax = SyntaxAnalyser(token_list, ls)
        if syntax_result(syntax):
            id_list = SemanticAnalyser(token_list_backup, lse, ts).verify_semantic()
            inter_code = IntermediateCode(id_list, token_list_backup, tci, lci).generate_intermediate_code()
            final_code = FinalRaspberry(inter_code, id_list, lgc).generate_final_code()

    file = open('files_fonte/finalresult.s', 'w')
    for line in final_code:
        file.writelines(line + '\n')
    file.close()


fun_compiler()

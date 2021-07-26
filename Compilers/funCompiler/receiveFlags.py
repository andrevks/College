import argparse
from typing import NamedTuple

'''
   Options:
      An option, sometimes called a flag or a switch, 
      is intended to modify the behavior of the program. 
      
   Arguments:
      Also called operands or parameters.The arguments represent the source 
      or the destination of the data that the command acts on.
      
   -lt : imprime a listagem dos tokens
       Exemplo: $ compilador.py -lt arquivoErro.fonte
          onde:
            -lt parâmetro para imprimir a listagem dos tokens
             arquivoErro.fonte é o arquivo texto, com o código fonte do programa
             
   -tudo : exibe todas as listagens do compilador
   
   -lt : exibe  a listagem dos Tokens

   -as : exibe a árvore sintática (se for implementada)

   -ls  exibe o LOG do analisador sintático

'''

parser = argparse.ArgumentParser(description='Fun Compiler.')

parser.add_argument('-tudo',
                    dest='tudo',
                    action='store_true',
                    help='Exibe todas as listagens do compilador.')

parser.add_argument('-lt',
                    dest='ltokens',
                    action='store_true',
                    help='Exibe a listagem dos Tokens.')

parser.add_argument('-ls',
                    dest='lsintatico',
                    action='store_true',
                    help='Exibe o LOG do analisador sintático.')

parser.add_argument('-lse',
                    dest='lsemantico',
                    action='store_true',
                    help='Exibe o LOG do analisador semântico.')

parser.add_argument('-ts',
                    dest='tsimbolos',
                    action='store_true',
                    help='Exibe a tabela de símbolos.')

parser.add_argument('-tci',
                    dest='tintermediario',
                    action='store_true',
                    help='Exibe a tabela do código intermediário')

parser.add_argument('-lci',
                    dest='lintermediario',
                    action='store_true',
                    help='Exibe o LOG do código intermediário')

parser.add_argument('-lgc',
                    dest='lgeracao',
                    action='store_true',
                    help='Exibe o LOG da geração de código.')

# file required argument
parser.add_argument('filename', help='Required: Informe um caminho para um arquivo')
args = parser.parse_args()

try:
    with open(args.filename, "r") as file:
        source_code = file.read()
except IOError and FileNotFoundError as err:
    print("Arquivo não encontrado! " + err)


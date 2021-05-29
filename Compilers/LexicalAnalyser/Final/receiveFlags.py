import argparse
from sys import argv

'''
   Options:
      An option, sometimes called a flag or a switch, 
      is intended to modify the behavior of the program. 
      
   Arguments:
      Also called operands or parameters.The arguments represent the source 
      or the destination of the data that the command acts on.
      
   -lt : imprime a listagem dos tokens
       Exemplo: $ compilador.py -lt arquivo.fonte
          onde:
            -lt parâmetro para imprimir a listagem dos tokens
             arquivo.fonte é o arquivo texto, com o código fonte do programa
   
'''

def flags(argv):

    parser = argparse.ArgumentParser()
    parser.add_argument('-lt', '--listartokens',
                        dest='iofile',
                        help='Send a file',
                        type=str)

    args = parser.parse_args()
    file_path = args.iofile
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except IOError and FileNotFoundError as err:
        print("Arquivo não encontrado! " + err)


flags(argv)

from sys import argv
from receiveFlags import flags
from typing import NamedTuple
import re


class LexicalError:

    def __init__(self, line, col, lex, msg):
        self.__line = line
        self.__col = col
        self.__lex = lex
        self.__msg = msg
        self.print_error()

    def print_error(self):
        print('\n----------------------|ERRO|-----------------------')
        print(f'Tipo de erro: "ERRO LÉXICO" \n'
              f'Padrão: \'  {self.__lex}  \' inesperado na' 
              f' linha {self.__line} e coluna {self.__col}\n'
              f'Descrição: {self.__msg}')
        print('---------------------------------------------------\n')


class Token(NamedTuple):
    type: str
    lexeme: str
    line: int
    col: int


class LexicalAnalyser:

    def __init__(self, source_code):
        self.__source_code = source_code

        self.__keywords = {
            'BeginFun', 'EndFun', 'if', 'then', 'else', 'elif',
            'end', 'funLoopWhile', 'do', 'endFunLoop',
            'showMeTheCode', 'grabInput', 'funny'
        }

        self.__keywords1 = {
            'BEGINFUN', 'ENDFUN', 'IF', 'THEN', 'ELSE', 'ELIF',
            'END', 'FUNLOOPWHILE', 'DO', 'ENDFUNLOOP',
            'SHOWMETHECODE', 'GRABINPUT', 'FUNNY'
        }

        self.__token_pair = [
            ('TK_NUM', r'\b\d+\b'),
            ('TK_ATRIB', r'<-'),
            ('TK_PERIOD', r'\.'),
            ('TK_ID', r'[A-Za-z]([A-Za-z]|\d|_)*'),
            ('TK_STRING', r'"[^"\\\r\n]*(?:\\.[^"\\\r\n]*)*"'),  # String com aspas
            ('TK_OP_AR', r'[-+*\/]'),  # Operações aritmética
            ('TK_OP_RE', r'<>|[=<>]'),  # Operação relacional
            ('TK_BOOL', r'[|&]'),
            ('TK_OPEN_P', r'\('),
            ('TK_CLOSE_P', r'\)'),
            ('TK_COMMA', r','),
            ('TK_NEW_LINE', r'\n'),
            ('TK_SKIP', r'[\ \t\r]+'),
            ('MISMATCH', r'.')
        ]

    def generate_token(self):

        token_base = self.__token_pair
        buffer = self.__source_code
        # Cria grupos com o nome de cada par de token no formato: (?P<nomeTk>regex)
        # Concatena cada par com '|' que vai servir como OU em passos seguintes
        # regex_rules se torna uma string concatenada com todos os grupos em regex
        regex_rules = '|'.join('(?P<%s>%s)' % strPair for strPair in token_base)
        line = 1
        col_start = 0

        # tk_type: Pega o nome do padrão reconhecido mais recente. Dependendo
        # do padrão existem algumas correções antes de salvar como um token
        # lexeme: pega o valor extraído quando o padrão é reconhecido
        # column: calcula o valor inicial da coluna do token encontrado
        for matchedPattern in re.finditer(regex_rules, buffer):
            tk_type = matchedPattern.lastgroup
            lexeme = matchedPattern.group()
            column = (matchedPattern.start() + 1) - col_start
            if tk_type == 'TK_NUM':
                lexeme = int(lexeme)
            elif lexeme.upper() in self.__keywords1 and tk_type == 'TK_ID':
                if lexeme not in self.__keywords:
                    LexicalError(line, column, lexeme, " Palavra chave ")
                tk_type = lexeme
            elif tk_type == 'TK_NEW_LINE':
                col_start = matchedPattern.end()
                line += 1
                continue
            elif tk_type == 'TK_SKIP':
                continue
            elif tk_type == 'MISMATCH':
                LexicalError(line, column, lexeme, "Formato de token NÃO registrado")
                continue

            # Retorna uma função geradora a quem chamou. A execução começa
            # apenas quando o gerador é iterado
            # Vantagem: Nenhuma memória é alocada quando o yield é usado
            # O parâmetro é uma tupla nomeada (NamedTuple)
            yield Token(tk_type, lexeme, line, column)


def main():
    # content = flags(argv)
    content = open('arquivo.fonte').read()
    lexico = LexicalAnalyser(content).generate_token()
    print("TOKENS:")
    print("( TOKEN ,  LEXEMA,  LINHA  , COLUNA)")
    lexico_copy = lexico
    lexico_queue = []
    for token in lexico:
        # print(f'( {token.type}, {token.lexeme}, {token.line}, {token.col} )')
        lexico_queue.append(token)
    end_of_file = Token('$', '$', 100, 1)
    lexico_queue.append(end_of_file)
    return lexico_queue




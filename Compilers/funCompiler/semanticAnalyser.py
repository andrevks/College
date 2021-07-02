from hashTable import HashTable

class SemanticError(Exception):
    def __init__(self, line, col, lex = '', msg = 'ERRO SEMÂNTICO !'):
        self.__line = line
        self.__col = col
        self.__msg = msg
        self.__lex = lex
        self.print_error()

    def print_error(self):
        print('\n----------------------|ERRO|-----------------------')
        print(f'Tipo de erro: "ERRO SEMÂNTICO" \n'
              f'Linha {self.__line} e Coluna {self.__col}\n'
              f'Descrição: {self.__msg}\n'
              f'Próximo ao padrão  \'  {self.__lex}  \' ou o próprio padrão')
        print('---------------------------------------------------\n')

class Symbol:
    def __init__(self, var, value, line, location):
        self.var = var
        self.value = value
        self.line = line
        self.location = location

class SemanticAnalyser:

    def __init__(self,tokens):
        self.__symbol_table = HashTable()
        self.__token_list = tokens


    def insert(self , lexeme, line, value , location):
        new_var = Symbol(lexeme,value,line,location)
        print("New VAR: ",new_var.var)
        key = new_var.var
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table(self, key):
        return self.__symbol_table.find(key).var == key;

    # def verify(self):


    def verify_semantic(self):
        l_index = 0
        for token in self.__token_list:
            # print(token.lexeme)
            # print(token.line)
            # print(token.type)
            # print("---------\n")
            self.insert(token.lexeme,token.line,0,l_index)
            l_index += 1

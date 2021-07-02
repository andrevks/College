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
              f'Token \'  {self.__lex}  \'')
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
        print("\n-----------INSERT------------")
        print("VARIÁVEL A SER DECLARADA: ",new_var.var)
        print("line: ", new_var.line)
        print("location: ",new_var.location)
        print("-----------------------------\n")
        key = new_var.var
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table(self, key):
        print("\n-----------TABLE------------")
        print("Encontrar chave: ", key)
        check = False
        try:
            print("Está na tabela ? ", self.__symbol_table.find(key).var == key)
            print("-----------------------------\n")
            check = self.__symbol_table.find(key).var == key;
            return check
        except AttributeError as att:
            raise
            check = False

    # def verify(self):


    def verify_semantic(self):
        l_index = 0
        tok = self.__token_list
        while l_index < len(tok):
            lex = tok[l_index].lexeme
            line = tok[l_index].line
            type = tok[l_index].type
            col = tok[l_index].col

            #DECLARAÇÃO DE VARIÁVEL
            if type == 'funny':
                #put the variables on the table
                l_index_bu = l_index + 1
                while tok[l_index_bu].lexeme != '.' :

                    if tok[l_index_bu].type == 'TK_ID':
                        lex = tok[l_index_bu].lexeme
                        line = tok[l_index_bu].line
                        self.insert(lex,line,0,l_index_bu)
                    elif tok[l_index_bu].type == 'TK_ATRIB':
                        break
                    l_index_bu += 1
                # continue
            elif type == 'TK_ID':
                var = lex
                # if not self.is_var_on_table(var):
                #     print("ERRO SEMÂNTICO !")
                print("\n----------ENCONTROU VAR-------------")
                print("LEX antes da checagem: ", lex)
                try:
                    if self.is_var_on_table(var):
                        print("Variável foi declarada")
                except AttributeError as att:
                    SemanticError(line , col , lex ,f'Variável NÃO declarada: ( {att} )')
                    print("-----------------------------\n")
                # continue
            l_index += 1

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
              f'Variável: \'  {self.__lex}  \'')
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
        print("Inserir variável")
        print("VARIÁVEL A SER DECLARADA: ",new_var.var)
        key = new_var.var
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table(self, key):
        check = False
        try:
            print("Está na tabela ? ", self.__symbol_table.find(key).var == key)
            print("Encontrar Variavel")
            check = self.__symbol_table.find(key).var == key;
            return check
        except AttributeError as att:
            raise
            check = False

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
                print("\nDECLARAR VARIÁVEL")
                l_index_bu = l_index + 1
                while tok[l_index_bu].lexeme != '.':

                    if tok[l_index_bu].type == 'TK_ID':
                        lex = tok[l_index_bu].lexeme
                        line = tok[l_index_bu].line
                        #se ta na tabela é != None
                        if self.__symbol_table.find(lex) == None :
                            self.insert(lex,line,0,l_index_bu)
                        else:
                            SemanticError(line , col , lex , f'Variável Duplicada')
                    elif tok[l_index_bu].type == 'TK_ATRIB':
                        break

                    # elif tok[l_index_bu].type == 'TK_ATRIB':
                    #     if not tok[l_index_bu + 2].type == 'TK_PERIOD':
                    #         continue
                    #     if tok[l_index_bu+1].type == 'TK_ID':
                    #         var = tok[l_index+1].var
                    #         if self.__symbol_table.find(var) == None :
                    #             self.insert(lex,line,0,l_index_bu)
                    #
                    #
                    #     if tok[l_index+1].type == 'TK_NUM':

                        break
                    l_index_bu += 1
            elif type == 'TK_ID':
                print("\nENCONTROU VARIÁVEL")
                try:
                    var = lex
                    if self.is_var_on_table(var):
                        print("Variável foi declarada")
                except AttributeError as att:
                    SemanticError(line , col , lex ,f'Variável NÃO Declarada: ( {att} )')

            elif type == 'TK_ATRIB':

                #Apenas interessado em variável com uma var ou num.
                if not tok[l_index + 2].type == 'TK_PERIOD':
                    l_index += 1
                    continue
                if tok[l_index+1].type == 'TK_NUM':
                    num = tok[l_index+1].lexeme
                    var = tok[l_index-1].lexeme
                    print(f'Num {num} to Var value: {var} ')
                    #Supondo que a var existe na tabela:
                    var_value = self.__symbol_table.find(var).value = num
                    print(f'Var value is {var_value}')

                if tok[l_index+1].type == 'TK_ID':
                    right_var= tok[l_index+1].lexeme
                    left_var = tok[l_index-1].lexeme
                    print(f'Right Var {right_var} to Left Var value: {left_var} ')
                    right_var_value = self.__symbol_table.find(right_var).value
                    result = self.__symbol_table.find(left_var).value = right_var_value

                    print(f'Var value is {result} ')



            l_index += 1

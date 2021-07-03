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
              f'Variável/Padrão: \'  {self.__lex}  \'')
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
        self.__history_table = []


    def insert(self , lexeme, line, value , location):
        new_var = Symbol(lexeme,value,line,location)
        key = new_var.var
        print(f"\nInserir variável ({key})")
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table(self, key):
        # print("Verificar VAR na Tabela")
        # check = False
        # try:
        #     print("Buscar Variavel")
        #     check = self.__symbol_table.find(key).var == key;
        #     return check
        # except AttributeError as att:
        #     raise
        #     check = False
        print("\nVerificar VAR na Tabela")
        print("Buscar Variavel\n")
        return self.__symbol_table.find(key) != None;



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
                while tok[l_index_bu].lexeme != '.':

                    if tok[l_index_bu].type == 'TK_ID':
                        lex = tok[l_index_bu].lexeme
                        line = tok[l_index_bu].line
                        #se ta na tabela é != None
                        print("\nBuscar Variavel\n")
                        if self.__symbol_table.find(lex) == None :
                            self.insert(lex,line,0,l_index_bu)
                        else:
                            SemanticError(line , col , lex , f'Variável Duplicada')
                    elif tok[l_index_bu].type == 'TK_ATRIB':
                        break

                    l_index_bu += 1
            elif type == 'TK_ID':
                var = lex
                if not self.is_var_on_table(var):
                    SemanticError(line , col , lex ,f'Variável NÃO Declarada')

            elif type == 'TK_ATRIB':
                #Apenas interessado em variável com uma var ou num.
                if not tok[l_index + 2].type == 'TK_PERIOD':
                    l_index += 1
                    continue
                right_var = tok[l_index + 1].lexeme
                left_var = tok[l_index - 1].lexeme
                if tok[l_index+1].type == 'TK_NUM':
                    num = right_var
                    var = left_var
                    print(f'{var} <- {num}')
                    #Supondo que a var existe na tabela:
                    print("\nBuscar Variavel\n")
                    var_value = self.__symbol_table.find(var).value = num
                    print(f'{var} == {var_value}')

                if tok[l_index+1].type == 'TK_ID':
                    print(f' {left_var} <- {right_var}')
                    print("\nBuscar Variavel\n")
                    right_var_value = self.__symbol_table.find(right_var).value
                    print("\nBuscar Variavel\n")
                    result = self.__symbol_table.find(left_var).value = right_var_value
                    print(f'{left_var} == {result} ')

            elif 'TK_OP_AR' and lex == '/':
                print("DIVISÃO !!!!")

                right_var = tok[l_index + 1]
                lex = right_var.lexeme
                col = right_var.col
                if right_var.type == 'TK_ID':
                    print("\nBuscar Variavel\n")
                    right_var_value = self.__symbol_table.find(right_var.lexeme).value
                    if right_var_value == 0:
                        SemanticError(line , col , lex , f'Divisão por ZERO')
                elif right_var.lexeme == 0:
                    SemanticError(line , col , lex , f'Divisão por ZERO')

            l_index += 1

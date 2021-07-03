from hashTable import HashTable
import hashTable

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

    def __init__(self, tokens, lse, ts):
        self.__symbol_table = HashTable()
        self.__token_list = tokens
        self.__keys_history = []



    def switch_mode(self,lse,ts):
        if lse:
            print("\n---------------Analisador Semântico--------------\n")
            print("\nLOG DE OPERAÇÕES:\n")
            self.verify_semantic_log(ts)
        elif ts:
            self.verify_semantic_log(ts)
        else:
            self.verify_semantic()


    def insert_log(self , lexeme, line, value , location):
        new_var = Symbol(lexeme,value,line,location)
        key = new_var.var
        numbers = new_var.value
        self.__keys_history.append(key)
        print(f"Inserir variável ({key})\n")
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table_log(self, key):
        print("\nVerificar VAR na Tabela")
        print("Buscar Variavel\n")
        return self.__symbol_table.find(key) != None;

    def show_symbol_table_log(self,ts):
        if ts:
            print("\n---------------------TABELA DE SÍMBOLOS-------------------")
            print('{:<20}  {:<10} {:<10}'.format('Variáveis' , 'Valor', 'linha'))
            print('{:<20}  {:<10} {:<10}'.format('----------' , '------', '-----'))
            for key in self.__keys_history:

                var_value = self.__symbol_table.find(key).value
                var = self.__symbol_table.find(key).var
                line = self.__symbol_table.find(key).line
                print('{:<20}  {:<10} {:<10}'.format(var,var_value,line))


    def verify_semantic_log(self,ts):
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
                        print("Buscar Variavel\n")
                        if self.__symbol_table.find(lex) == None :
                            self.insert_log(lex,line,0,l_index_bu)
                        else:
                            SemanticError(line , col , lex , f'Variável Duplicada')
                    elif tok[l_index_bu].type == 'TK_ATRIB':
                        break

                    l_index_bu += 1
            elif type == 'TK_ID':
                var = lex
                if not self.is_var_on_table_log(var):
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
                    #Supondo que a var existe na tabela:
                    print("Buscar Variavel\n")
                    var_value = self.__symbol_table.find(var).value = num
                    print(f'Atribuir valor({var_value}) a Var({var})')

                if tok[l_index+1].type == 'TK_ID':
                    print("Buscar Variavel\n")
                    right_var_value = self.__symbol_table.find(right_var).value
                    print("Buscar Variavel\n")
                    result = self.__symbol_table.find(left_var).value = right_var_value
                    print(f'Atribuir valor ({result}) a Var{left_var}')

            elif 'TK_OP_AR' and lex == '/':
                right_var = tok[l_index + 1]
                lex = right_var.lexeme
                col = right_var.col
                if right_var.type == 'TK_ID':
                    print("Buscar Variavel\n")
                    right_var_value = self.__symbol_table.find(right_var.lexeme).value
                    if right_var_value == 0:
                        SemanticError(line , col , lex , f'Divisão por ZERO')
                elif right_var.lexeme == 0:
                    SemanticError(line , col , lex , f'Divisão por ZERO')

            l_index += 1
        self.show_symbol_table_log(ts)

    '''
        ---------------- Default ---------------- 
    '''

    def insert(self , lexeme, line, value , location):
        new_var = Symbol(lexeme,value,line,location)
        key = new_var.var
        self.__symbol_table.insert(key,new_var)

    def is_var_on_table(self, key):
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
                        if self.__symbol_table.find(lex) == None :
                            self.insert(lex,line,0,l_index_bu)
                        else:
                            SemanticError(line , col , lex , f'Variável Duplicada')
                    elif tok[l_index_bu].type == 'TK_ATRIB':
                        break

                    l_index_bu += 1

            #EXISTÊNCIA DE VARIÁVEL
            elif type == 'TK_ID':
                var = lex
                if not self.is_var_on_table(var):
                    SemanticError(line , col , lex ,f'Variável NÃO Declarada')

            #ATRIBUIÇÃO
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
                    #Supondo que a var existe na tabela:
                    var_value = self.__symbol_table.find(var).value = num

                if tok[l_index+1].type == 'TK_ID':
                    right_var_value = self.__symbol_table.find(right_var).value
                    result = self.__symbol_table.find(left_var).value = right_var_value

            # DIVISÃO POR ZERO
            elif 'TK_OP_AR' and lex == '/':

                right_var = tok[l_index + 1]
                lex = right_var.lexeme
                col = right_var.col
                if right_var.type == 'TK_ID':
                    right_var_value = self.__symbol_table.find(right_var.lexeme).value
                    if right_var_value == 0:
                        SemanticError(line , col , lex , f'Divisão por ZERO')
                elif right_var.lexeme == 0:
                    SemanticError(line , col , lex , f'Divisão por ZERO')

            l_index += 1

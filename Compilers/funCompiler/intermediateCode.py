from infixPostfix import StackInfix

class IntermediateCode:
    def __init__(self, variable_list, tokens_list):
        self.__variables = variable_list
        self.__tokens_list = tokens_list
        # self.__log_inter_code = []
        self.__intermediate_code = []
        self.convert = StackInfix()
        self.generate_intermediate_code()



    def generate_intermediate_code(self):
        tok = self.__tokens_list
        comand = ''
        l_index = 0
        #pegar variáveis declaradas
        print("\n-----------VAR LIST----------")
        for var in self.__variables:
            self.__intermediate_code.append(f'_Var {var}')
        print(self.__variables)
        while l_index < len(tok):
            lex = tok[l_index].lexeme
            line = tok[l_index].line
            type = tok[l_index].type
            col = tok[l_index].col

            if lex == 'grabInput':
              comand = 'leia'
              while tok[l_index].lexeme != '.':
                if tok[l_index].type == 'TK_ID':
                    lex = tok[l_index].lexeme
                    self.__intermediate_code.append(f'{comand} {lex}')
                l_index += 1
            elif type == 'TK_ATRIB':
                var = tok[l_index - 1].lexeme
                infix_exp = ''
                l_index += 1
                while tok[l_index].lexeme != '.':
                    lex = tok[l_index].lexeme
                    # print(f'LEX: {lex} and STR(lex): {str(lex)}')
                    infix_exp += str(lex)
                    l_index += 1
                print("INFIX: ", infix_exp)
                postfix_exp = self.convert.infixToPostfix(infix_exp)
                print("POSTFIX: ", postfix_exp)
                self.__intermediate_code.append(f'{var} = {postfix_exp}')
            elif lex == 'funLoopWhile':
                comand = 'enquanto'
                endcmd = 'faca'
                bool_exp = ''
                l_index += 1
                while tok[l_index].lexeme != 'do':
                    lex = tok[l_index].lexeme
                    bool_exp += ' ' + str(lex)
                    l_index += 1
                self.__intermediate_code.append(f'\n{comand}{bool_exp} {endcmd}')
            elif lex == 'endFunLoop':
                comand = 'fim_enquanto'
                self.__intermediate_code.append(f'{comand}')
            elif lex == 'if':
                comand = 'se'
                endcmd = 'entao'
                bool_exp = ''
                l_index += 1
                while tok[l_index].lexeme != 'then':
                    lex = tok[l_index].lexeme
                    print("lex: ", lex)
                    bool_exp += ' ' + str(lex)
                    l_index += 1
                self.__intermediate_code.append(f'\n{comand}{bool_exp} {endcmd}')
            elif lex == 'else':
                comand = 'senao'
                self.__intermediate_code.append(f'{comand}')
            elif lex == 'end':
                comand = 'fim_se'
                self.__intermediate_code.append(f'{comand}')
            elif lex == 'showMeTheCode':
                comand = 'escreva'
                bool_exp = ''
                l_index += 1
                while tok[l_index].lexeme != '.':
                    lex = tok[l_index].lexeme
                    print("lex: ", lex)
                    bool_exp += ' ' + str(lex)
                    l_index += 1
                self.__intermediate_code.append(f'{comand}{bool_exp}')
            l_index += 1

        print("\n---------CÓDIGO INTERMEDIÁRIO---------")
        for codeline in self.__intermediate_code:
            print(codeline)
        return self.__intermediate_code
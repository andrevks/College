from infixPostfix import StackInfix

class IntermediateCode:
    def __init__(self, variable_list, tokens_list):
        self.__variables = variable_list
        self.__tokens_list = tokens_list
        self.__log_inter_code = []
        self.__intermediate_code = []
        self.convert = StackInfix()
        self.generate_intermediate_code()

    def set_log(self,log):
        self.__log_inter_code.append(log)


    def show_log(self):
        for logline in self.__log_inter_code:
            print(logline)


    def show_intermediate_code(self):
        print('\n---------CÓDIGO INTERMEDIÁRIO---------')
        for codeline in self.__intermediate_code:
            print(codeline)



    def generate_intermediate_code(self):
        tok = self.__tokens_list
        comand = ''
        l_index = 0
        #pegar variáveis declaradas
        self.set_log('\n--LOG: CÓDIGO INTERMEDIÁRIO')
        for var in self.__variables:
            self.__intermediate_code.append(f'_Var {var}')
            self.set_log(f'Montou a variável ({var})')
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
                    self.set_log('Reconheceu o comando de leitura (grabInput)')
                l_index += 1
            elif type == 'TK_ATRIB':
                var = tok[l_index - 1].lexeme
                infix_exp = ''
                l_index += 1
                while tok[l_index].lexeme != '.':
                    lex = tok[l_index].lexeme
                    infix_exp += str(lex)
                    l_index += 1
                postfix_exp = self.convert.infixToPostfix(infix_exp)
                self.set_log(f'Fez a conversão infixa para posfixa')
                self.__intermediate_code.append(f'{var} = {postfix_exp}')
                self.set_log(f'Reconheceu uma atribuição de variável ({var}<- {postfix_exp})')
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
                self.set_log(f'Reconheceu o comando enquanto e faca (funLoopWhile ({bool_exp}) do)')
            elif lex == 'endFunLoop':
                comand = 'fim_enquanto'
                self.__intermediate_code.append(f'{comand}')
                self.set_log('Reconheceu o comando fim_enquanto (endFunLoop)')
            elif lex == 'if':
                comand = 'se'
                endcmd = 'entao'
                bool_exp = ''
                l_index += 1
                while tok[l_index].lexeme != 'then':
                    lex = tok[l_index].lexeme
                    bool_exp += ' ' + str(lex)
                    l_index += 1
                self.__intermediate_code.append(f'\n{comand}{bool_exp} {endcmd}')
                self.set_log(f'Reconheceu o comando se e então (if({bool_exp}) then)')
            elif lex == 'else':
                comand = 'senao'
                self.__intermediate_code.append(f'{comand}')
                self.set_log('Reconheceu o comando senao (else)')
            elif lex == 'end':
                comand = 'fim_se'
                self.__intermediate_code.append(f'{comand}')
                self.set_log('Reconheceu o comando fim_se (end)')
            elif lex == 'showMeTheCode':
                comand = 'escreva'
                bool_exp = ''
                l_index += 1
                while tok[l_index].lexeme != '.':
                    lex = tok[l_index].lexeme
                    bool_exp += ' ' + str(lex)
                    l_index += 1
                self.__intermediate_code.append(f'{comand}{bool_exp}')
                self.set_log(f'Reconheceu o comando escreva (showMeTheCode ({bool_exp}))')
            l_index += 1

        self.show_log()
        self.show_intermediate_code()
        return self.__intermediate_code


import lexicalAnalyser

#Representing the big table
SYNTAX_TABLE = {
    '<PROGRAMA>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': 0, 'EndFun':'',
                    'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
                    'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
                    'do':'','endFunLoop':'','TK_BOOL':'','TK_OP_AR': '','TK_OP_RE':''
                    },
    '<LISTA_COMANDOS>':{'$': '', 'TK_ID': 1,'TK_NUM': '' , 'TK_STRING': '', 'BeginFun': '', 'EndFun':2,
                          'TK_PERIOD':1,'TK_ATRIB':'','TK_COMMA':1, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':1,
                          'grabInput':1,'funny': 1,'if':1,'then':'','else': 2,'end': 2, 'funLoopWhile':1,'do':'',
                          'endFunLoop':2,'TK_BOOL': '','TK_OP_AR': '','TK_OP_RE': ''
                          },
    '<COMANDO>':{'$': '', 'TK_ID': 8,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
                   'TK_PERIOD':3,'TK_ATRIB':'','TK_COMMA':3, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':13,
                   'grabInput':3,'funny': 8,'if':18,'then':'','else':'', 'end': '','funLoopWhile':21,
                   'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
                   },
    '<ANT_VAR>':{'$': '', 'TK_ID':12 ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
                   'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
                   'grabInput':'','funny': 11,'if':'','then':'','else':'', 'end': '','funLoopWhile':'',
                   'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
                   },
    '<DPS_VAR>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
               'TK_PERIOD':10,'TK_ATRIB':9,'TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
               'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','funLoopWhile':'',
               'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
               },
    '<INPUT>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':5,'TK_ATRIB':'','TK_COMMA':5, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':4,'funny': '','if':'','then':'','else':'', 'end': '','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<DISPLAY>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
           'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':14,
           'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','funLoopWhile':'',
           'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
           },
    '<DISPLAY_F>': {'$': '', 'TK_ID':15 ,'TK_NUM': '' ,'TK_STRING': 16, 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<KEY>':{'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':7,'TK_ATRIB':'','TK_COMMA':6, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       },
    '<ELSE>':{'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':19, 'end':20,'funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
        },
    '<STRING>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': 17, 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          },
    '<OPER>' : {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 24,'TK_OP_RE':''
        },
    '<OPER_REL>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
            'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
            'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
            'do':'','endFunLoop':'','TK_BOOL': 29,'TK_OP_AR':'', 'TK_OP_RE': 28
            },
    '<OPERAN>': {'$': '', 'TK_ID':33 ,'TK_NUM': 34,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          },
    '<EXP>': {'$': '', 'TK_ID':22 ,'TK_NUM': 22 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':23, 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       },
    '<EXP_F>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
         'TK_PERIOD':25,'TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':25,'showMeTheCode':'',
         'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
         'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 26,'TK_OP_RE':''
         },
    '<EXPR_BOOL>': {'$': '', 'TK_ID':27 ,'TK_NUM': 27 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<BOOL_F>': {'$': '', 'TK_ID': '','TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':32,'else': '','end': '','funLoopWhile':'',
          'do':32,'endFunLoop':'','TK_BOOL': 31,'TK_OP_AR': '','TK_OP_RE': 31
          },
    '<BOOL_TYPE>' : {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL':30,'TK_OP_AR': '','TK_OP_RE':''
             }
}

class SyntaxError(Exception):
    def __init__(self, line, col, lex = '', msg = 'ERRO SINTÁTICO !'):
        self.__line = line
        self.__col = col
        self.__msg = msg
        self.__lex = lex
        self.print_error()

    def print_error(self):
        print('\n----------------------|ERRO|-----------------------')
        print(f'Tipo de erro: "ERRO SINTÁTICO" \n'
              f'Linha {self.__line} e Coluna {self.__col}\n'
              f'Descrição: {self.__msg}\n'
              f'Próximo ao padrão  \'  {self.__lex}  \' ou o próprio padrão')
        print('---------------------------------------------------\n')


class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.__top = None
        self.__elem = 0

    def isEmpty(self):
        return self.__top == None

    def peek(self):
        return self.__top.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.__top
        self.__top = new_node
        self.__elem +=1

    def pop(self):
        if self.isEmpty():
            return None
        deleted_node = self.__top
        self.__top = deleted_node.next
        deleted_node.next = None
        self.__elem -= 1
        return deleted_node.data

class SyntaxAnalyser:

    def __init__(self, tokens, log):
        self.__tokens = tokens
        self.__syntax_table_values = {
                      0: 'BeginFun <LISTA_COMANDOS> EndFun', 1: '<COMANDO> TK_PERIOD <LISTA_COMANDOS>',
                      2: '#', 3: '<INPUT>',
                      4: 'grabInput TK_ID <KEY>', 5: '<KEY>', 6: 'TK_COMMA TK_ID <INPUT>', 7: '#',
                      8: '<ANT_VAR> TK_ID <DPS_VAR>',
                      9: 'TK_ATRIB <EXP>', 10: '#', 11: 'funny', 12: '#', 13: '<DISPLAY>',
                      14: 'showMeTheCode <DISPLAY_F>',
                      15: 'TK_ID', 16: '<STRING>', 17: 'TK_STRING',
                      18: 'if <EXPR_BOOL> then <LISTA_COMANDOS> <ELSE> end',
                      19: 'else <LISTA_COMANDOS>', 20: '#',
                      21: 'funLoopWhile <EXPR_BOOL> do <LISTA_COMANDOS> endFunLoop', 22: '<OPERAN> <EXP_F>',
                      23: 'TK_OPEN_P <EXP> TK_CLOSE_P <EXP_F>', 24: 'TK_OP_AR <EXP>',
                      25: '#', 26: '<OPER>',
                      27: '<OPERAN> <BOOL_F>',
                      28: 'TK_OP_RE <EXPR_BOOL>', 29: '<BOOL_TYPE> <EXPR_BOOL>', 30: 'TK_BOOL', 31: '<OPER_REL>',
                      32: '#', 33: 'TK_ID',
                      34: 'TK_NUM' }
        self.__syntax_table = SYNTAX_TABLE

    def switch_mode(self,log):
        if log:
            print("\n---------------Analisador Sintático--------------\n")
            print("\nLOG DE OPERAÇÕES:\n")
            self.initiate_stack_log()
            self.recognise_sentence_log()
            return self.tokens_recognised_log()
        else:
            self.initiate_stack()
            self.recognise_sentence()
            return self.tokens_recognised()

    def initiate_stack_log(self):
        self.__stack = Stack()
        print("Empilhar $")
        self.__stack.push('$')
        print("Empilhar Não-Terminal Inicial \n")
        self.__stack.push('<PROGRAMA>')

    def tokens_recognised_log(self):
        print("Verificar Pilha Vazia")
        print("Verificar Estado da Lista")
        return self.__stack.isEmpty() and not self.__tokens

    def error_verification_log(self,top_stack, first_elem):
        tk_line = self.__tokens[0].line
        tk_col = self.__tokens[0].col
        lex = self.__tokens[0].lexeme

        if self.__stack.isEmpty() and self.__tokens:
            print("Verificar Pilha Vazia")
            print("Verificar Estado da Lista")
            SyntaxError(tk_line, tk_col, lex, 'PILHA VAZIA e ainda há elementos na LISTA')
        elif not self.__stack.isEmpty() and len(self.__tokens) == 0:
            print("Verificar Pilha Vazia")
            print("Verificar Estado da Lista")
            SyntaxError(tk_line, tk_col, lex, 'LISTA VAZIA e ainda há elementos na Pilha')
        else:
            SyntaxError(tk_line, tk_col, lex, f'Não encontrou um elemento correspondente na tabela - {top_stack}:{first_elem}')


    def consult_table_log(self, line, col):
        print("Buscar Indice na Tabela Sintática")
        rules_index = self.__syntax_table[line][col]
        # prodution found
        if rules_index == '':
            self.error_verification_log(line,col)
        print("Retornar Produção Encontrada")
        rule = self.__syntax_table_values[rules_index]
        # pop the last element of the stack
        print("Desempilhar")
        self.__stack.pop()
        # split the whole rule
        rule = rule.split()
        max = len(rule)
        for i in range(max):
            # send element in opposite order to the stack
            rule_to_stack = rule.pop()
            if rule_to_stack == '#':
                continue
            print("Empilhar Produção: ", rule_to_stack)
            self.__stack.push(rule_to_stack)


    def recognise_sentence_log(self):
        index = 0
        try:
            while not self.tokens_recognised_log() :
                print('Consultar Topo')
                top_stack= self.__stack.peek()
                print('Consultar Elemento da Lista')
                first_elem = self.__tokens[index].type
                if top_stack == first_elem :
                    print("Desempilhar")
                    self.__stack.pop()
                    print("Remover Elemento da Lista")
                    self.__tokens.pop(0) #removing first token
                elif self.__syntax_table[top_stack][first_elem] != None:
                    self.consult_table_log(top_stack,first_elem)
                print('\n')
        except Exception as ex:
            self.error_verification_log(top_stack, first_elem)

    '''
        ---------------- Default ---------------- 
    '''
    def initiate_stack(self):
        self.__stack = Stack()
        self.__stack.push('$')
        self.__stack.push('<PROGRAMA>')

    def tokens_recognised(self):
        return self.__stack.isEmpty() and not self.__tokens

    def error_verification(self,top_stack, first_elem):
        tk_line = self.__tokens[0].line
        tk_col = self.__tokens[0].col
        lex = self.__tokens[0].lexeme

        if self.__stack.isEmpty() and self.__tokens:
            SyntaxError(tk_line, tk_col, lex, 'PILHA VAZIA e ainda há elementos na LISTA')
        elif not self.__stack.isEmpty() and len(self.__tokens) == 0:
            SyntaxError(tk_line, tk_col, lex, 'LISTA VAZIA e ainda há elementos na Pilha')
        else:
            SyntaxError(tk_line, tk_col, lex, f'Não encontrou um elemento correspondente na tabela - {top_stack}:{first_elem}')


    def consult_table(self, line, col):
        rules_index = self.__syntax_table[line][col]
        # prodution found
        if rules_index == '':
            self.error_verification(line,col)
        rule = self.__syntax_table_values[rules_index]
        # pop the last element of the stack
        self.__stack.pop()
        # split the whole rule
        rule = rule.split()
        max = len(rule)
        for i in range(max):
            # send element in opposite order to the stack
            rule_to_stack = rule.pop()
            if rule_to_stack == '#':
                continue
            self.__stack.push(rule_to_stack)


    def recognise_sentence(self):
        index = 0
        try:
            while not self.tokens_recognised() :
                top_stack= self.__stack.peek()
                first_elem = self.__tokens[index].type
                if top_stack == first_elem :
                    self.__stack.pop()
                    self.__tokens.pop(0) #removing first token
                elif self.__syntax_table[top_stack][first_elem] != None:
                    self.consult_table(top_stack,first_elem)
        except Exception as ex:
            self.error_verification(top_stack, first_elem)
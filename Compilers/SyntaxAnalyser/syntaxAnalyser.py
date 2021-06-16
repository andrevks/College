import lexicalAnalyser

#Representing the big table
SYNTAX_TABLE = {
    '<PROGRAMA>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': 0, 'EndFun':'',
                    'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
                    'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
                    'do':'','endFunLoop':'','TK_BOOL':'','TK_OP_AR': '','TK_OP_RE':''
                    },
    '<LISTA_COMANDOS>':{'$': '', 'TK_ID': 1,'TK_NUM': '' , 'TK_STRING': '', 'BeginFun': '', 'EndFun':2,
                          'TK_PERIOD':1,'TK_ATRIB':'','TK_COMMA':1, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':1,
                          'grabInput':1,'funny': 1,'if':1,'then':'','else': 2,'end': 2, 'elif': 2,'funLoopWhile':1,'do':'',
                          'endFunLoop':2,'TK_BOOL': '','TK_OP_AR': '','TK_OP_RE': ''
                          },
    '<COMANDO>':{'$': '', 'TK_ID': 8,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
                   'TK_PERIOD':3,'TK_ATRIB':'','TK_COMMA':3, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':13,
                   'grabInput':3,'funny': 8,'if':18,'then':'','else':'', 'end': '','elif': '','funLoopWhile':23,
                   'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
                   },
    '<ANT_VAR>':{'$': '', 'TK_ID':12 ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
                   'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
                   'grabInput':'','funny': 11,'if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
                   'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
                   },
    '<DPS_VAR>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
               'TK_PERIOD':10,'TK_ATRIB':9,'TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
               'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
               'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
               },
    '<INPUT>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':5,'TK_ATRIB':'','TK_COMMA':5, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':4,'funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<DISPLAY>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
           'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':14,
           'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
           'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
           },
    '<DISPLAY_F>': {'$': '', 'TK_ID':15 ,'TK_NUM': 15 ,'TK_STRING': 16, 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<KEY>':{'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':7,'TK_ATRIB':'','TK_COMMA':6, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       },
    '<ELSE>':{'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':19, 'end':20,'elif': '','funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
        },
    '<ELIF>' :{'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':22, 'end':22,'elif': 21,'funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
        },
    '<STRING>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': 17, 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          },
    '<OPER>' : {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 26,'TK_OP_RE':''
        },
    '<OPER_REL>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
            'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
            'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
            'do':'','endFunLoop':'','TK_BOOL': 31,'TK_OP_AR':'', 'TK_OP_RE': 30
            },
    '<OPERAN>': {'$': '', 'TK_ID':35 ,'TK_NUM': 36 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          },
    '<EXP>': {'$': '', 'TK_ID':24 ,'TK_NUM': 24 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':25, 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       },
    '<EXP_F>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
         'TK_PERIOD':27,'TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':27,'showMeTheCode':'',
         'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
         'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 28,'TK_OP_RE':''
         },
    '<EXPR_BOOL>': {'$': '', 'TK_ID':29 ,'TK_NUM': 29 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             },
    '<BOOL_F>': {'$': '', 'TK_ID': 34,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':34,'TK_ATRIB':'','TK_COMMA':34, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':34,
          'grabInput':34,'funny': 34,'if':34,'then':34,'else': 34,'end': 34,'elif': '','funLoopWhile':34,
          'do':34,'endFunLoop':'','TK_BOOL': 33,'TK_OP_AR': '','TK_OP_RE': 33
          },
    '<BOOL_TYPE>' : {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL':32,'TK_OP_AR': '','TK_OP_RE':''
             }
}

class SyntaxError:

    def __init__(self, line, col, msg):
        self.__line = line
        self.__col = col
        self.__msg = msg
        self.print_error()

    def print_error(self):
        print('\n----------------------|ERRO|-----------------------')
        print(f'Tipo de erro: "ERRO SINTÁTICO" \n'
              f' linha {self.__line} e coluna {self.__col}\n'
              f'Descrição: {self.__msg}')
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

    def __init__(self, tokens):
        self.__tokens = tokens
        self.initiate_stack()
        self.__syntax_table_values = {
                      0: 'BeginFun <LISTA_COMANDOS> EndFun', 1: '<COMANDO> TK_PERIOD <LISTA_COMANDOS>',
                      2: '#', 3: '<INPUT>',
                      4: 'grabInput TK_ID <KEY>', 5: '<KEY>', 6: 'TK_COMMA TK_ID <INPUT>', 7: '#',
                      8: '<ANT_VAR> TK_ID <DPS_VAR>',
                      9: 'TK_ATRIB <EXP>', 10: '#', 11: 'funny', 12: '#', 13: '<DISPLAY>',
                      14: 'showMeTheCode <DISPLAY_F>',
                      15: '<EXPR_BOOL>', 16: '<STRING>', 17: 'TK_STRING',
                      18: 'if <EXPR_BOOL> then <LISTA_COMANDOS> <ELIF> <ELSE> end',
                      19: 'else <LISTA_COMANDOS>', 20: '#', 21: 'elif <EXPR_BOOL> <LISTA_COMANDOS>', 22: '#',
                      23: 'funLoopWhile <EXPR_BOOL> do <LISTA_COMANDOS> endFunLoop', 24: '<OPERAN> <EXP_F>',
                      25: 'TK_OPEN_P <EXP> TK_CLOSE_P <EXP_F>', 26: 'TK_OP_AR <EXP>', 27: '#', 28: '<OPER>',
                      29: '<OPERAN> <BOOL_F>',
                      30: 'TK_OP_RE <EXPR_BOOL>', 31: '<BOOL_TYPE> <EXPR_BOOL>', 32: 'TK_BOOL', 33: '<OPER_REL>',
                      34: '#', 35: 'TK_ID',
                      36: 'TK_NUM' }
        self.__syntax_table = SYNTAX_TABLE


    def initiate_stack(self):
        self.__stack = Stack()
        self.__stack.push('$')
        self.__stack.push('<PROGRAMA>')

    def tokens_recognised(self):
        return self.__stack.isEmpty() and not self.__tokens

    def consult_table(self, line, col):

        try:
            rules_index = self.__syntax_table[line][col]
            # prodution found
            rule = self.__syntax_table_values[rules_index]
            print("rule: ", rule)
            # pop the last element of the stack
            self.__stack.pop()
            # split the whole rule
            rule = rule.split()
            print("rule: ", rule)
            max = len(rule)
            for i in range(max):
                # send element in opposite order to the stack
                rule_to_stack = rule.pop()
                print("Rule to STACK: ", rule_to_stack)
                if rule_to_stack == '#':
                    continue
                self.__stack.push(rule_to_stack)
        except KeyError as err:
            raise SyntaxError(line, col, "Não encontrou um elemento correspodente na tabela")

    def recognise_sentence(self):
        index = 0
        try:
            while not self.tokens_recognised() :
                top_stack= self.__stack.peek()
                first_elem = self.__tokens[index].type
                print('TOP STACK: ',top_stack)
                print('FIRST ELEM QUEUE: ',first_elem)

                if self.__stack.peek() == tokens[index].type :
                    self.__stack.pop()
                    removed_token = tokens.pop(0) #removing first token
                    print("Removed token: ", removed_token)
                    print("CURRENT TOKEN LIST:", tokens)
                elif self.__syntax_table[top_stack][first_elem] != None:
                    self.consult_table(top_stack,first_elem)
                print("-------------------------- \n")
        except :
            raise SyntaxError(tokens[index].line , tokens[index].col, "ERRO Sintático no loop")


if __name__ == '__main__':

    tokens = lexicalAnalyser.main()
    syntaxAnaliser = SyntaxAnalyser(tokens)
    syntaxAnaliser.recognise_sentence()
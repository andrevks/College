

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
                   'grabInput':11,'funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
                   'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
                   },

    '<DPS_VAR>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
               'TK_PERIOD':10,'TK_ATRIB':9,'TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
               'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
               'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
               },
    '<INPUT>': {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':5,'TK_ATRIB':'','TK_COMMA':5, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':4,
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
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

syntax_table_dict = { 0: 'BeginFun <LISTA_COMANDOS> EndFun', 1: '<COMANDO> TK_PERIOD <LISTA_COMANDOS>',
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

if __name__ == '__main__':

    # s = Stack()
    #
    # print(s.isEmpty())
    # s.push('<PROGRAMA>')
    # s.push('<LISTA_COMANDO>')
    # s.push('ELSE')
    # s.push('funLoopWhile')
    # print("REMOVED: ",s.pop())
    # print("REMOVED: ",s.pop())
    # print("REMOVED: ",s.pop())
    # print("PEEK: ",s.peek())
    #
    # print(s.isEmpty())
    file_path = 'list_syntax_table'
    content = ''
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except IOError and FileNotFoundError as err:
        print("Arquivo não encontrado! " + err)

    # str = '<PROGRAMA> ::= BeginFun <LISTA_COMANDOS> EndFun'

    print(SYNTAX_TABLE['<BOOL_F>']['TK_PERIOD'])








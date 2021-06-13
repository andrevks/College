#
# class SyntaxAnalyser:
#
#     def __init__(self, syntax_table):
#         self.__syntax_table = syntax_table
#         self.

PROGRAM = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': 0, 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL':'','TK_OP_AR': '','TK_OP_RE':''
             }

LISTA_COMANDOS = {'$': '', 'TK_ID': 1,'TK_NUM': '' , 'TK_STRING': '', 'BeginFun': '', 'EndFun':2,
        'TK_PERIOD':1,'TK_ATRIB':'','TK_COMMA':1, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':1,
        'grabInput':1,'funny': 1,'if':1,'then':'','else': 2,'end': 2, 'elif': 2,'funLoopWhile':1,'do':'',
        'endFunLoop':2,'TK_BOOL': '','TK_OP_AR': '','TK_OP_RE': ''
        }

COMANDO = {'$': '', 'TK_ID': 8,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':3,'TK_ATRIB':'','TK_COMMA':3, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':13,
          'grabInput':3,'funny': 8,'if':18,'then':'','else':'', 'end': '','elif': '','funLoopWhile':23,
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          }

ANT_VAR = {'$': '', 'TK_ID':12 ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
           'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
           'grabInput':11,'funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
           'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
           }
DPS_VAR = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
           'TK_PERIOD':10,'TK_ATRIB':9,'TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
           'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
           'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
           }
INPUT = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
           'TK_PERIOD':5,'TK_ATRIB':'','TK_COMMA':5, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':4,
           'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
           'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
           }
DISPLAY = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
         'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':14,
         'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
         'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
         }
DISPLAY_F = {'$': '', 'TK_ID':15 ,'TK_NUM': 15 ,'TK_STRING': 16, 'BeginFun': '', 'EndFun':'',
         'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
         'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
         'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
         }
KEY = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':7,'TK_ATRIB':'','TK_COMMA':6, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end': '','elif': '','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
             }
ELSE = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':19, 'end':20,'elif': '','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       }

ELIF = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':22, 'end':22,'elif': 21,'funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
        }

STRING = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': 17, 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
        }

OPER = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 26,'TK_OP_RE':''
          }
OPER_REL = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
        'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
        'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
        'do':'','endFunLoop':'','TK_BOOL': 31,'TK_OP_AR':'', 'TK_OP_RE': 30
        }
OPERAN = {'$': '', 'TK_ID':35 ,'TK_NUM': 36 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          }
EXP = {'$': '', 'TK_ID':24 ,'TK_NUM': 24 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':25, 'TK_CLOSE_P':'','showMeTheCode':'',
          'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
          'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
          }
EXP_F = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':27,'TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':27,'showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': 28,'TK_OP_RE':''
       }
EXPR_BOOL = {'$': '', 'TK_ID':29 ,'TK_NUM': 29 ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
       'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
       'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
       'do':'','endFunLoop':'','TK_BOOL': '','TK_OP_AR': '','TK_OP_RE':''
       }
BOOL_F = {'$': '', 'TK_ID': 34,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
          'TK_PERIOD':34,'TK_ATRIB':'','TK_COMMA':34, 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':34,
          'grabInput':34,'funny': 34,'if':34,'then':34,'else': 34,'end': 34,'elif': '','funLoopWhile':34,
          'do':34,'endFunLoop':'','TK_BOOL': 33,'TK_OP_AR': '','TK_OP_RE': 33
          }
BOOL_TYPE = {'$': '', 'TK_ID':'' ,'TK_NUM': '' ,'TK_STRING': '', 'BeginFun': '', 'EndFun':'',
             'TK_PERIOD':'','TK_ATRIB':'','TK_COMMA':'', 'TK_OPEN_P':'', 'TK_CLOSE_P':'','showMeTheCode':'',
             'grabInput':'','funny': '','if':'','then':'','else':'', 'end':'','elif':'','funLoopWhile':'',
             'do':'','endFunLoop':'','TK_BOOL':32,'TK_OP_AR': '','TK_OP_RE':''
             }


#
#
# class Stack

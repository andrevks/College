from receiveFlags import args
from receiveFlags import source_code
from lexicalAnalyser import LexicalAnalyser
from syntaxAnalyser import SyntaxAnalyser

class Compiler(args,source_code,object):

    def __init__(self, LexicalAnalyser, SyntaxAnalyser):
        self.tudo = args.tudo
        self.lt = args.ltokens
        self.ls = args.lsintatico
        self.watch_cmd()

    def watch_cmd(self):
        print(f"FLAGS: tudo: {self.tudo}, ltoken: {self.lt}, lsintatico: {self.ls}")

    def run_compiler(self):
        tokens = LexicalAnalyser(source_code, self.lt)
        SyntaxAnalyser(tokens, True)


if __name__ == '__main__':
    lex = LexicalAnalyser(source_code)
    syntax = SyntaxAnalyser(lex)
    Compiler(lex,)

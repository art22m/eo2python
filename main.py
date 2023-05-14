import sys
from antlr4 import *
from ProgramLexer import ProgramLexer
from ProgramParser import ProgramParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ProgramLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ProgramParser(stream)
    tree = parser.program()
    print(1)


if __name__ == '__main__':
    main(sys.argv)
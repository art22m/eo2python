
build:
	antlr -Dlanguage=Python3 Program.g4

clean:
	rm ProgramParser.py
	rm ProgramListener.py
	rm ProgramLexer.tokens
	rm ProgramLexer.py
	rm ProgramLexer.interp
	rm Program.tokens
	rm Program.interp
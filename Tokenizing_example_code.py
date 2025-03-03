source_code = 'int x = 42'
lexer = Lexer(source_code)
tokens = lexer.tokenize()

print(tokens)

import re

# Define token patterns
token_patterns = {
    'NUMBER': r'\d+',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'ASSIGN': r'=',
    'TYPE': r'(int|float|char|void)',
    'OPERATOR': r'[+\-*/]',
    'DELIMITER': r'[(),;{}]',
    'WHITESPACE': r'\s+',
}

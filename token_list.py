TOKEN_PATTERNS = {
    'KEYWORD': r'\b(?:' + '|'.join(KEYWORDS) + r')\b',  # Match any keyword
    'IDENTIFIER': IDENTIFIER,                           # Match identifiers
    'OPERATOR': '|'.join(OPERATORS.values()),           # Match all operators
    'DELIMITER': DELIMITERS,                            # Match delimiters
    'NUMBER': LITERALS['NUMBER'],                       # Match numbers
    'STRING': LITERALS['STRING'],                       # Match strings
    'CHARACTER': LITERALS['CHARACTER'],                 # Match characters
    'BOOLEAN': LITERALS['BOOLEAN'],                     # Match boolean literals
    'NULL': LITERALS['NULL'],                           # Match null literals
    'TYPE': TYPES,                                     # Match types
    'SINGLE_LINE_COMMENT': COMMENTS['SINGLE_LINE'],     # Match single-line comments
    'MULTI_LINE_COMMENT': COMMENTS['MULTI_LINE'],       # Match multi-line comments
    'WHITESPACE': WHITESPACE,                           # Match whitespace
    'PUNCTUATION': PUNCTUATION,                         # Match punctuation
    'SPECIAL': SPECIAL,                                 # Match special tokens
}

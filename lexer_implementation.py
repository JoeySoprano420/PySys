class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def get_token(self):
        if self.position >= len(self.source_code):
            return None

        for token_type, pattern in token_patterns.items():
            regex = re.compile(pattern)
            match = regex.match(self.source_code, self.position)

            if match:
                value = match.group(0)
                self.position += len(value)
                if token_type != 'WHITESPACE':
                    self.tokens.append((token_type, value))
                return (token_type, value)

        raise SyntaxError(f"Invalid character: {self.source_code[self.position]}")

    def tokenize(self):
        while self.position < len(self.source_code):
            self.get_token()

        return self.tokens

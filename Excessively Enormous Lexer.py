import re

class EnormousLexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.tokens = []
        self.token_patterns = {
            'KEYWORDS': r'\b(def|if|else|for|while|return|class|try|except|import|from|continue|break|and|or|not|pass|lambda|yield|del|global|assert|with|is|None|True|False)\b',
            'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
            'NUMBER': r'\b\d+\b',
            'FLOAT': r'\b\d+\.\d+\b',
            'STRING': r'\".*?\"|\'[^\']*\'',
            'CHARACTER': r'\'.\'',
            'COMMENT_SINGLE': r'#.*',
            'COMMENT_MULTI': r'"""(.*?)"""|\'\'\'(.*?)\'\'\'',
            'OPERATOR': r'[+\-*/%=<>!&|^~]',
            'ASSIGNMENT': r'=' ,
            'PUNCTUATION': r'[.,;:()]',
            'BRACKETS': r'[\[\]{}]',
            'WHITESPACE': r'\s+',
        }

    def tokenize(self):
        """
        Tokenizes the input code by matching it with the regex patterns for various token types.
        """
        position = 0
        while position < len(self.input_code):
            match = None
            for token_type, pattern in self.token_patterns.items():
                regex = re.compile(pattern)
                match = regex.match(self.input_code, position)
                if match:
                    value = match.group(0)
                    if token_type != 'WHITESPACE':  # Ignore whitespaces
                        self.tokens.append((token_type, value))
                    position = match.end()
                    break
            if not match:
                raise ValueError(f"Unexpected character at position {position}: {self.input_code[position]}")
    
    def get_tokens(self):
        """
        Returns the list of tokens after lexing.
        """
        return self.tokens
    
    def display_tokens(self):
        """
        Displays all tokens along with their types.
        """
        for token_type, value in self.tokens:
            print(f"{token_type}: {value}")
    
    def generate_token_summary(self):
        """
        Generates a summary of the token counts by type.
        """
        summary = {}
        for token_type, value in self.tokens:
            if token_type not in summary:
                summary[token_type] = 1
            else:
                summary[token_type] += 1
        return summary

    def generate_token_report(self):
        """
        Generates a detailed report of all tokens.
        """
        summary = self.generate_token_summary()
        print("Token Summary Report:")
        for token_type, count in summary.items():
            print(f"{token_type}: {count} instances")
        print("\nFull Token List:")
        self.display_tokens()


# Example Usage
source_code = """
def add(a, b):
    # This is a simple addition function
    if a > b:
        return a + b
    else:
        return a - b

x = 10
y = 5.5
z = 'Hello, World!'

# A while loop
while x > y:
    x -= 1

"""  # Example source code

# Instantiate and tokenize the source code
lexer = EnormousLexer(source_code)
lexer.tokenize()

# Display the tokenized result
lexer.display_tokens()

# Generate and display a summary report
lexer.generate_token_report()

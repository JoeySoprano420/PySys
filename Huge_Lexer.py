import re
import threading
import time
import sys
from collections import deque


# **HIGHLY-DOMINANT AND OVER-POWERED LEXER WITH AMPLE FORTITUDE**

class OverpoweredLexer:
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
            'SPECIAL': r'[\@\$#\^&\*\(\)]',  # Additional symbols or special characters
            'ESCAPE_SEQUENCE': r'\\[abfnrtv\\"\'0-9]',  # Escape sequences in strings
            'HEX_NUMBER': r'\b0x[0-9A-Fa-f]+\b',  # Hexadecimal numbers
            'BINARY_NUMBER': r'\b0b[01]+\b',  # Binary numbers
        }

    def tokenize(self):
        """
        Tokenizes the input code by matching it with the regex patterns for various token types.
        """
        position = 0
        code_length = len(self.input_code)
        
        # Optimized lexical analysis with context-sensitive matching
        while position < code_length:
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
                # Handle unexpected characters or syntax errors
                self.tokens.append(('ERROR', f"Unexpected character at position {position}: {self.input_code[position]}"))
                position += 1

    def parallel_tokenize(self):
        """
        Tokenize using multi-threading for faster processing, especially for larger input sizes.
        """
        def worker(start, end):
            segment = self.input_code[start:end]
            lexer_segment = OverpoweredLexer(segment)
            lexer_segment.tokenize()
            return lexer_segment.tokens

        threads = []
        num_threads = 4
        segment_length = len(self.input_code) // num_threads

        for i in range(num_threads):
            start = i * segment_length
            end = start + segment_length if i != num_threads - 1 else len(self.input_code)
            thread = threading.Thread(target=lambda idx=i: threads.append(worker(start, end)))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Merge all tokens from different threads and sort by position
        all_tokens = deque()
        for thread_tokens in threads:
            all_tokens.extend(thread_tokens)
        
        self.tokens = sorted(all_tokens, key=lambda x: self.input_code.index(x[1]))

    def optimize(self):
        """
        Uses more advanced strategies like caching token patterns to improve tokenization speed
        """
        self.token_patterns = {key: re.compile(pattern) for key, pattern in self.token_patterns.items()}

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

    def get_tokens(self):
        """
        Returns the list of tokens after lexing.
        """
        return self.tokens

# Test Code (for the lexer)

source_code = """
def add(a, b):
    # Addition function with basic error checking
    if a > b:
        return a + b
    else:
        return a - b

x = 10
y = 5.5
z = 'Hello, World!'

while x > y:
    x -= 1

"""

lexer = OverpoweredLexer(source_code)

start_time = time.time()
lexer.tokenize()  # Standard tokenization
lexer.parallel_tokenize()  # Optimized multi-threaded tokenization
lexer.optimize()  # Apply further optimizations
end_time = time.time()

lexer.generate_token_report()

print("\nProcessing time:", end_time - start_time)

import re

def tokenize(source_code):
    position = 0
    tokens = []
    
    while position < len(source_code):
        match = None
        
        for token_type, pattern in TOKEN_PATTERNS.items():
            regex = re.compile(pattern)
            match = regex.match(source_code, position)
            
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':  # Skip whitespace
                    tokens.append((token_type, value))
                position += len(value)
                break
        
        if not match:
            raise SyntaxError(f"Unexpected character at position {position}")
    
    return tokens

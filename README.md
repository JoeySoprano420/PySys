# PySys

### **Overview of Current Progress**

The goal is to create a **cumulative-learning iterative-procedural compiler (C.L.I.P. Compiler)** for a superscript of Python that is optimized for low-level dominance, using **MSVC**, **NASM**, and **Python 13+**. We've been moving through the design and implementation stages, focusing primarily on the **lexical analysis** part of the compiler development, with careful attention to ensure we can handle low-level constructs, without relying on external dependencies like LLVM, g++, or MLIR.

Here's what we've accomplished so far:

---

### **1. High-Level Architecture**

The compiler is designed to be modular and efficient, with **low-level dominance** being a key focus. The idea is to allow Python-like syntax with low-level control, making it suitable for systems programming, embedded systems, and scenarios where direct memory management and performance are paramount.

---

### **2. Lexical Analysis (Lexer)**

We’ve implemented the **lexical analysis** stage, which involves breaking down the source code into meaningful chunks or **tokens**. These tokens are the building blocks for subsequent stages of the compiler (parsing, optimization, and code generation).

#### **Tokens Defined So Far:**

1. **Keywords (Reserved Words)**:
   - A list of essential keywords like `int`, `if`, `else`, `for`, `while`, `void`, `true`, `false`, `struct`, `typedef`, etc.
   
2. **Identifiers**:
   - Tokens that match variable names, function names, class names, etc. They start with letters or underscores and may contain digits.

3. **Operators**:
   - Arithmetic: `+`, `-`, `*`, `/`, etc.
   - Logical: `&&`, `||`, `!`, etc.
   - Comparison: `==`, `!=`, `>`, `<`, etc.
   - Bitwise: `&`, `|`, `^`, `~`, etc.
   - Assignment: `=`, `+=`, `-=`, `*=`, etc.
   - Increment/Decrement: `++`, `--`

4. **Delimiters**:
   - These tokens include common symbols used for structure, such as `()`, `{}`, `[]`, `;`, etc.

5. **Literals**:
   - Numeric literals (both integer and floating-point), string literals, character literals, boolean literals, and `null`.

6. **Data Types**:
   - Basic types like `int`, `char`, `float`, `double`, `bool`, etc.

7. **Comments**:
   - Single-line (`//`) and multi-line (`/* */`) comments to ensure proper skipping during tokenization.

8. **Whitespace**:
   - Spaces, tabs, and newlines are handled and ignored during tokenization.

9. **Punctuation**:
   - Basic punctuation marks like commas and periods for structuring code.

10. **Special Tokens**:
    - Special characters that may be used for specific extensions or features, such as `@`, `$`, and `&`.

#### **Regular Expressions for Tokens:**
To match these tokens, we have defined **regex patterns** that correspond to each category. For example:
- **Keywords**: A word boundary match for predefined language keywords.
- **Identifiers**: Matching any sequence of characters that starts with a letter or an underscore, followed by letters, digits, or underscores.
- **Operators**: Various regex patterns to match arithmetic, logical, and assignment operators.
- **Literals**: Regex patterns to match numeric, string, and boolean literals.
- **Comments**: Matching both single-line and multi-line comments.

---

### **3. Tokenization Process**

We’ve written a **tokenizer** function that takes the source code as input and returns a list of tokens. The process is as follows:
1. **Reading the source code**: The code is parsed from the beginning to the end, character by character.
2. **Matching tokens**: At each step, the lexer tries to match the current character sequence against the regular expressions for different token types.
3. **Skipping invalid characters**: If a match is found, it’s added to the list of tokens, and the lexer moves forward. If no match is found, a syntax error is raised.
4. **Handling whitespace**: Whitespace is ignored during tokenization, and only meaningful tokens are collected.

---

### **4. Sample Input/Output**

For the input source code:
```python
int main() {
    int x = 42;
    if (x == 42) {
        x++;
    }
}
```

The lexer generates the following tokens:
```plaintext
[('KEYWORD', 'int'), ('IDENTIFIER', 'main'), ('DELIMITER', '('), 
('DELIMITER', ')'), ('DELIMITER', '{'), ('KEYWORD', 'int'), 
('IDENTIFIER', 'x'), ('ASSIGN', '='), ('NUMBER', '42'), 
('DELIMITER', ';'), ('KEYWORD', 'if'), ('DELIMITER', '('), 
('IDENTIFIER', 'x'), ('COMPARISON', '=='), ('NUMBER', '42'), 
('DELIMITER', ')'), ('DELIMITER', '{'), ('IDENTIFIER', 'x'), 
('INCREMENT_DECREMENT', '++'), ('DELIMITER', ';'), ('DELIMITER', '}'), 
('DELIMITER', '}')]
```

---

### **5. Next Steps in Development**

We are currently at the **lexical analysis** phase, where the goal is to ensure that the lexer can correctly identify all meaningful components of the source code. 

The next steps are:
1. **Parsing**: Once the tokens are generated, the next step is to parse them into an Abstract Syntax Tree (AST) or some other internal representation.
2. **Handling Errors**: We will need to ensure that invalid tokens or unexpected sequences of characters result in meaningful error messages to guide the developer.
3. **Optimization**: Consider adding optimization features, like removing unnecessary tokens or simplifying expressions early on.
4. **Code Generation**: Convert the AST into assembly code or machine code using **NASM** and **MSVC**, and generate executables for the target platform.

---

### **Conclusion**

So far, we’ve built a solid foundation by defining key language constructs and setting up the tokenization process. With the lexer now handling the identification of a broad array of tokens, we are ready to move towards parsing, code generation, and other advanced features as we continue developing this compiler.

Would you like to continue with the parsing phase or refine the lexer further?

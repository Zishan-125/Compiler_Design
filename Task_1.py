import re

def tokenize_and_identify(input_string):
    
    
    token_patterns = [
        ('KEYWORD',    r'\b(int|float|and|or|if|else|while)\b'),
        ('NUMBER',     r'\b\d+\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('OPERATOR',   r'[=\+\-\*/]'),
        ('PUNCTUATION',r';'),
        ('WHITESPACE', r'\s+'),
    ]

  
    master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
    
    print(f"{'Token':<15} | {'Type':<15}")
    print("-" * 33)

    for match in re.finditer(master_pattern, input_string):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        
        
        if token_type != 'WHITESPACE':
            print(f"{token_value:<15} | {token_type:<15}")


input_text = "int sum=10; and a+b= 20;"
tokenize_and_identify(input_text)
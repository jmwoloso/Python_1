#!/usr/local/bin/python3
"""Secret code generated from user input."""

code_src = input('Message: ')
out_code = []

for k,v in enumerate(code_src):
    out_code.append((chr(ord(v) + 1)))
reversed(out_code)  
print(''.join(reversed(out_code)))
#!/usr/local/bin/python3
"""Program that demonstrates the ability to write
   and use custom functions to manipulate a string
   supplied by the user"""

import sys

def sys_exit(inp_2):
    print('-'*40)
    print('Goodbye for now!')
    print('-'*40)
    return sys.exit()

if __name__ == "__main__":
    switch = {
        'capitalize': str.capitalize,
        'title': str.title,
        'upper': str.upper,
        'lower': str.lower,
        'exit': sys_exit
    }

    options = switch.keys()
    prompt_1 = "Enter a function name ({0}): ".format(', '.join(options))
    prompt_2 = "Enter a string: "
    
    while True:
        inp_1 = input(prompt_1).lower()
        if not inp_1 or inp_1 not in switch.keys():                           #validating that input is supplied at all and/or that supplied input matches available options
            print('-'*40)
            print('Please choose a valid option...')
            print('-'*40)
            continue
        
        inp_2 = input(prompt_2)
        if not inp_2:
            print('-'*40)
            print('Please enter a string...')
            print('-'*40)
            continue
        option = switch.get(inp_1, None)
            
        if option:
            print(switch[inp_1](inp_2))
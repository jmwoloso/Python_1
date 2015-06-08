#!/usr/local/bin/python3
"""Saves user-input and then writes it to a file."""

ofile = open('user_input.txt', 'a')
ofile.close()

while True:
    open_file = open('user_input.txt', 'r')
    for i, txt in enumerate(open_file):
        print(txt)
    
    string_input = input('Enter text: ')
    if not string_input:                             
        break
    
    elif string_input:
        new_txt = open('user_input.txt', 'a')
        new_txt.write(string_input)
        new_txt.close()
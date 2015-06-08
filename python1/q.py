#!/usr/local/bin/python3
"""Quiz program that returns lowercase string from input"""
def lo_case(string):
    string = string.lower()
    print("This is now lowercase: {0}".format(string))

string = input('Enter text in all-CAPS: ')
lo_case(string)
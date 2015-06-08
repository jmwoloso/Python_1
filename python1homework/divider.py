#!/usr/local/bin/python3
"""Tests understanding of exception handling."""

while True:
    x = 10
    inp = input('Provide an integer: ')
    try:
        print(10/int(inp))
        continue
    except ValueError:
        print('Your input must be an integer')
    except ZeroDivisionError:
        print('Your input must not be zero (0)')
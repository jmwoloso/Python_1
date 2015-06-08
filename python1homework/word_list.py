#!/usr/local/bin/python3
"""This program takes input from the user and creates a list of words based on the input."""

s = input("Please input a sentence: ")

words_upper = []	#initializing a list to put words containing at least one uppercase letter
words_lower = []	#initializing a list to put words containing no uppercase letters in
	
words = s.strip().split()

for word in words:
    if word.islower():
        words_lower.append(word)
                
    else:
        words_upper.append(word)

for word in words_upper + words_lower:
    print(word)
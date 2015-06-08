#!/usr/local/bin/python3
"""Deomstrates the ability to mercilessly refactor code."""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
titl = input("Enter a title: ")
word_lst = titl.title().split()                        #list created and title method applied to all words
spacer = ' '
return_title = []
for i, word in enumerate(word_lst[1:]):
    if word.lower() in small_words:
        word_lst[i+1] = word.lower()
        
print(spacer.join(word_lst))

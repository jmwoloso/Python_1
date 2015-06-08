#!/usr/local/bin/python3

"""This program takes user-input and creates a list
   of words, then adds each word to a set and a dict
   as a key with a value equal to the length set. The
   elements (words) of the dict are then displayed 
   along with the order each of them was discovered in."""

word_set = set()                
d = {}                       

while True:
    s = input("Enter text: ")
    if not s:
        print("Finished")
        break
    for punc in ',;.:?!"':
        s = s.replace(punc, "")
    
    word_list = s.lower().strip().split()

    for word in word_list:
        set_len = len(word_set)               # there is probably a simpler way to implement this
        word_set.add(word)
        curr_len = len(word_set)              # ditto
        if curr_len > set_len:
             d[word] = len(word_set)
#            d[word] = d.get(word, curr_len)  # I was going to use this to return the length until I tried your suggestion (see line before this one)
    
    for word in d.keys():
        print(word, d[word])

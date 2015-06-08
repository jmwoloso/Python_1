#!/usr/local/bin/python
"""Tests ability to build a complex program with minimal knowledge of Python."""

import sys



def main(argv):
    """Checks to see if the correct number of arguments were supplied to the script."""
    
    if len(argv) == 2:
        script, file_to_proc = argv
                                                                
    else:
        print("Please supply the correct number of arguments (2) and try again...")
        exit()



def word_length(word):
    """Calculates the length of each word in a list and assigns it as the index to the word length list."""
    
    word_len_lst[len(word)] += 1
    return word_len_lst


if __name__ == "__main__":
    main(sys.argv)                                                #passing the sys.argv list to the program

#////Opening file and initializing container objects...////    
    
    file_to_proc = sys.argv[1]                                    #assigns a name to the argument indexed at sys.argv[1] 
    file_to_proc = open(file_to_proc, 'r')                        #opens the file to read and process
    words = file_to_proc.read()                                   #empties the entire contents of the file 
    word_lst = []                                                 #initializing word list
    punc = ",.;:'!?&"                                             #list of punctuation characters to remove from text
    

#////Processing contents of file...////    
    
    for p in punc:
        words = words.replace(p, '')                              #removing punctuation marks
    word_lst = words.strip().split()                              #assigning words to the word list
    max_len = max(len(word) for word in word_lst) + 1             #maximum word length (+1) for initializing word length list
    word_len_lst = [0] * max_len                                  #initializing word length list by making list equal to one more than longest word length
    for word in word_lst:                                         #assigning word length to indices of word length list
        word_length(word)                                         #calling word length function and supplying each word in the word list as an argument
        #word_len_lst[len(word)] += 1                             #this was the original implementation I used before reading directions to create function to handle word length

    
#////Printing table of output from processed file...////
    
    print("Length Count")                                         #printing table headers     
    for i, ct in enumerate(word_len_lst):                         #iterating through word length list
        if ct:                                                    #verifying there are words of each length
            print("{0} {1}".format(i, ct))                        #printing word counts table
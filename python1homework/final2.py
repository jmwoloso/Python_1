#!/usr/local/bin/python3
"""Tests ability to build a complex program with minimal knowledge of Python."""

import sys                                                        #import sys to pass arguments to sys.argv

y_scale_factor = 20                                               #global variable; scale to use for y-axis levels; change to desired factor prior to execution
max_y_value = int()                                               #initializing container for largest y-axis value in histogram; do not alter
y_levels = int()                                                  #initializing container for number of levels (rows) to create output for; do not alter
y_levels_lst = []                                                 #initializing container for levels list
word_len_dct = dict()


#///Begin function definitions...///
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



def calc_vals(word_lengths, scale_factor):
    """Calculates values for use in printing the histogram to the desired scale."""
    
    """This was my initial attempt to make the histogram scalable according to whatever data may be supplied."""
    
    global max_y_value, y_levels                                  #identifying globals to be accessed outside of the function
    max_y_value = round(max(word_len_lst) * 1.5)                  #calculates (and then rounds) the highest value for the y-axis of the histogram
    y_levels = round(max_y_value / scale_factor)                  #calculates (and then rounds) the number of levels (iterations) that will be run through when printing
    return max_y_value, y_levels                                  #return calculated values for further use



def leveler(levels):
    """Creates the list with the appropriate levels list."""
    
    global y_levels_lst, y_scale_factor                           #identifying globals to be accessed outside of function
    y_levels_lst[levels] = levels * y_scale_factor                #replace elements with position number * scaling factor
    y_levels_lst.sort(reverse=True)                               #reverse the levels list
    return y_levels_lst                                           #return new list
  
    

def make_length_dct(word_lengths):
    """Creates the word length dictionary for use in printing."""
    
    global word_len_dct, word_len_lst                             #accessing global variables for calulations
    word_len_dct = {i+1 : n for i, n in enumerate(word_len_lst)}  #dict comp to add key, value pairs to dict
    return word_len_dct                                           #return word length dict for further use

   
        
#///END FUNCTION DEFINITIONS...///

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


#////Printing table of output from processed file...////
    
    print("Length   Count")                                       #printing table headers     
    for i, ct in enumerate(word_len_lst):                         #iterating through word length list
        if ct:                                                    #verifying there are words of each length
            print("{0:>7} {1:>7}".format(i, ct))                  #printing word counts table with padding and alignment info added
    print()
    
    
#////Creating and printing the histogram...////
    
    calc_vals(word_len_lst, y_scale_factor)                       #calling value calculation function
    
    y_levels_lst = [0] * (y_levels + 1)                           #filling levels list with placeholders
    for i, j in enumerate(y_levels_lst):                          
        leveler(i)                                                #passing placeholders to leveler function to be replaced  
        
          
#////Populating dict for printing...////
    
    make_length_dct(word_len_lst)                                 #creating the word length count dict
    bar = '-|'                                                    #formatting
    axis = '+--'                                                  #formatting
    for y in y_levels_lst:
        if y > 0:                                                        #used to manipulate 'x' axis formatting
            print("{0:>4} {1}".format(y, bar), end="")                   #Great suggestion about suppressing the newline, that was critical!
            for v in word_len_dct.values():                              
                if v >= y:                                               
                    column = "***"                                       
                else:                                                    
                    column = "   "                                         
                print(column, end="")
            print()
    print("{0:>4} -+-{1}+-".format(y_levels_lst[-1], axis * 15))
    print("        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16  ")           #'x' values for horizontal axis
    
#!/usr/local/bin/python3
"""Demonstrates ability to mercilessly refactor code."""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    word_lst = title.title().split()                        #list created and title method applied to all words
    spacer = ' '                                            #spacer created for use in join method later on
    for i, word in enumerate(word_lst[1:]):                 #iterate through list of words, ignoring first word
        if word.lower() in small_words:                     #lower method called for comparison to list of prepositions
            word_lst[i+1] = word.lower()                    #replace any words found to be in list of prepositions with
                                                            #their lower case equivalent and assign to appropriate index of original word list            
    new_title = spacer.join(word_lst)                       #concatenating our list of words together with a space in between
    return new_title                                        #send the result back to be evaluated

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
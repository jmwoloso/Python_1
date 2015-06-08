#!/usr/local/bin/python3
"""Tests ability to build a complex program with minimal knowledge of Python."""

import sys                                                        #import sys to pass arguments to sys.argv

y_scale_factor = 20                                               #global variable; scale to use for y-axis levels; change to desired factor prior to execution
#max_y_value = int()                                               #initializing container for largest y-axis value in histogram; do not alter
#y_levels = int()                                                  #initializing container for number of levels (rows) to create output for; do not alter
y_levels_dct = {}                                                 #initializing levels dict for iterating through during print operations


max_y_value = 400                  #calculates (and then rounds) the highest value for the y-axis of the histogram
y_levels = 20                  #calculates (and then rounds) the number of levels (iterations) that will be run through when printing
key = 1

for key in range(0, 21):
    y_levels_dct[key] = (key * y_scale_factor)
    key += 1
print(y_levels_dct)
        

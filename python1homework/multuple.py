#!/usr/local/bin/python3
"""Takes two-element tuples and prints the results of 
   multiplying the two numbers in each two-tuple."""
   
data = [
        (1, 1),
        (2, 2),
        (12, 13),
        (4, 4),
        (99, 98)]


fmt = "{0:>4} = {1:>2} x {2:>2}"       
for k, v in data:
    results = (k*v)
    print(fmt.format(results,k,v))
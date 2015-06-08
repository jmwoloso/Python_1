#!/usr/local/bin/python3
def my_func(a,b='b was not entered',c='c was not entered'):
    """3-parameter function."""
    print(a)
    print(b)
    print(c)

my_func('test')
my_func('test','test')
my_func('test','test','test')
print(my_func)
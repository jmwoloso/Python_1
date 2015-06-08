#!/usr/local/bin/python3
#
# check_string.py
#

"""
check_string.py takes user input and checks that it satisfies the conditions of the prompt
and then responds to the user depending on the input received. """
print(__doc__)
print(60 * "-")

#s = input("Please enter your favorite programming language in UPPER CASE, followed by a period: ")
#if "PYTHON" in s and s.endswith("."):
#    print("Hey! That's my favorite too! Great choice!")
#    print("Thanks for playing!")
#else:
#    print("I said to enter your FAVORITE programming language in UPPER CASE followed by a period!")
target = "PYTHON."
s = []
while s != target:
    s = input("Please enter your favorite programming language in UPPER CASE, followed by a period: ")
    print(80 * "-")
    if s.upper() in s and s.endswith("."):
        print(80 * "-")
        print("Hey! That's my favorite too! Great choice!")
        print("Thanks for playing!")
    else:
        print("I said to enter your FAVORITE programming language in UPPER CASE followed by a period!")
        print(80 * "-")   
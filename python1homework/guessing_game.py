#!/usr/local/bin/python3
"""Asks the user to guess the number that is randomly generated using the random() module."""
import random
rand_num = random.randint(1,99)

while True:
    user_num = input("Guess a number or press 'Enter' to quit: ")
    if not user_num:
        print("Thanks for playing!")
        break
    
    if not user_num.isdigit():
        print("That's not a number!")
        continue
    
    user_num = int(user_num)
    if user_num == rand_num:
        print('You guessed it!')
        break
    
    if user_num < rand_num:
        print('Too low')
                                   
    if user_num > rand_num:
        print('Too high')
        
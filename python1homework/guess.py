#!/usr/local/bin/python3
#
"""This program uses a 'while' loop to have the user guess a "secret" number and checks the number against the hidden value while terminating
after 5 incorrect guesses."""

secret = 10
guess = 0
max_guesses = 5
iteration = 0

while True:
    guess = int(input("Please guess the secret number (from 1 to 20): "))
    iteration += 1
    if guess < secret and iteration < max_guesses and iteration != (max_guesses - 1):
        print(\
             )   
        print(60 * "-")
        print("Too low...you have", (max_guesses - iteration), "chances left, please guess again...")
        print(60 * "-")
        print(\
             )
    elif guess < secret and iteration < max_guesses:
        print(\
             )   
        print(60 * "-")
        print("Too low...you have", (max_guesses - iteration), "chance left, please guess again...")
        print(60 * "-")
        print(\
             )
    elif guess > secret and iteration < max_guesses and iteration != (max_guesses - 1):
        print(\
             )   
        print(60 * "-")
        print("Too high...you have", (max_guesses - iteration), "chances left, please guess again...")
        print(60 * "-")
        print(\
             )
    elif guess > secret and iteration < max_guesses:
        print(\
             )   
        print(60 * "-")
        print("Too high...you have", (max_guesses - iteration), "chance left, please guess again...")
        print(60 * "-")
        print(\
             )                 
    elif guess == secret and iteration <= max_guesses:
        print(\
             )   
        print(60 * "-")
        print("You guessed the secret!")
        print("Thanks for playing!")
        print(60 * "-")
        print(\
             )   
        break
    else:
        print(\
             )   
        print(60 * "%")
        print(60 * "%")
        print(\
             )    
        print("Sorry, you have exceeded the maximum number of guesses...")
        print("The secret number was:", secret)
        print(\
             )
        print(60 * "%")
        print(60 * "%")
        print(\
             )  
        break      
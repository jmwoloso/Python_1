#!/usr/local/bin/python3
"""Demonstrates class and instance creation."""


dogs = []                                                                 #defined outside of the class, so its considered global by the class                                     

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def __str__(self):
        return "{0}:{1}".format(self.name, self.breed)                  
        #return "{0}. {1}:{2}".format(i, self.name, self.breed)            #an alternate I considered (see main loop below for explanation of why I didn't go with this code)
        
if __name__ == "__main__":
    while True:
        name_inp = input('Name: ')
        if not name_inp:
            break
        
        breed_inp = input('Breed: ')
        if not breed_inp:
            break
        new_dog = Dog(name_inp, breed_inp)
        dogs.append(new_dog) 
        print("DOGS")
        for i, dog in enumerate(dogs):               
            print("{0}. {1}".format(i,dog))      
            #print(dog)                                                     
        print('*' * 40)                                                     
        
        """I like the idea of a simple 'print(dog)' statement like you suggest, however to match the required output, I would need
        to include the 'index' reference within the str method in the Dog class. If the user doesn't supply call the index (i)
        every time the method is called, then an error would result, so I went with slightly more cumbersome line of code for 
        the print statement, but I believe it adds more integrity to the Dog class should its methods be needed later on in this code"""                     
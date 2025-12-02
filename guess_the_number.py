# Guess the Number

import os
import random

# Initalisation


secret_number = random.randint(1,100)
guess_count = 1
test = 1

# Clear the terminal screen
def set_up():
    os.system('clear')
    print("Guess the Number")
    print("----------------")
    print()
    print("I am thinking of a number between 1 and 100. Can you guess what it is?")



# Function to check guess against target number
def guess_check(guess, secret_number, guess_count):
    if guess == secret_number:
        print('Great, you took ' + str(guess_count) + ' attempts')
        print()
        return 1
    elif guess < secret_number:
            print("Higher!")
            print()
            return 0 
    else:
        print("Lower!")
        print()
        return 0

# Function to capture guess
def have_a_guess():
    guess = int(input("What is your guess?  "))
    print()
    return guess
    
    



set_up()


guess = have_a_guess()
test = guess_check(guess, secret_number, guess_count)

while test != 1:
    guess_count = guess_count + 1
    guess = have_a_guess()
    test = guess_check(guess, secret_number, guess_count)
    

    
 
        
    
    
    



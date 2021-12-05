"""ASS8 PROG2
Program 2: Guess the number
Generate 1 random number (0-100)
Ask the user to guess the number
Display “Greater than” if the inputed number is greater than the random number
Display “Less than” if the inputed number is less than the random number
Repeat asking the user until the random number has been guessed correctly."""

#Ass8 Prog2, 1st try,   working

import random

def ask_input():
    user_guess = input("Your guess:  ")
    
    while not user_guess.isdigit():
        print("\nOnly non-negative integers please. Try again. \n")
        user_guess = input("Your guess:  ")

    user_guess = int(user_guess)
    return user_guess

    
if __name__ == "__main__":

    #1 ask user guess with validity check
    print("\nTry to guess my special number (Clue: 0-100)")
    user_guess = ask_input()

    #2 generate a random number (0-100)
    my_number = random.randint(0, 100)
    print() #for checking ko lng kung ano laman nugn random number

    #3 let the user guess the random number
    while my_number != user_guess:
        if my_number > user_guess:
            print("Try guessing a higher number. \n")
            user_guess = ask_input()

        elif my_number < user_guess:
            print("Try guessing a lower number. \n")
            user_guess = ask_input()

    if my_number == user_guess:
        print("You guessed it right! \n")    

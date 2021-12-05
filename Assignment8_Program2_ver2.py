"""ASS8 PROG2
Program 2: Guess the number
Generate 1 random number (0-100)
Ask the user to guess the number
Display “Greater than” if the inputed number is greater than the random number
Display “Less than” if the inputed number is less than the random number
Repeat asking the user until the random number has been guessed correctly."""

#Ass8 Prog2, 1st try,   working
#            2nd try,   added super hint opt 

import random

def super_hint(): 
    super_hint_var = input("\nWould you like to use super hint? (Types 'y' for yes, 'n' for no):  ")

    if super_hint_var == "":
        super_hint_var = False
    elif super_hint_var[0].lower() == "y":
        super_hint_var = True
        print("Super hint activated! \nSuper hint will give you additional hints aside from the greater than or less than clues. ")
    else:
        super_hint_var = False
    return super_hint_var

def ask_input():
    user_guess = input("\nYour guess:  ")                                                

    while not user_guess.isdigit():
        print("Only non-negative integers please. Try again.")
        user_guess = input("\nYour guess:  ")

    user_guess = int(user_guess)                                    
    return user_guess

def hints(user_guess, my_number, super_hint):
    while my_number != user_guess:

        how_close = abs(user_guess - my_number)  
                  
        if super_hint == True:
            if how_close > 15:
                print("You are way off!")
            elif how_close > 10:
                print("You are getting there.")
            elif how_close > 5:
                print("You are getting close.")
            elif how_close > 2:
                print("You are close!")
            else:
                print("You are very close!")
        
        if user_guess > 100:                                               
            print("Clue: 0-100 only")
        elif my_number > user_guess:
            print("Try guessing a higher number.")
        elif my_number < user_guess:
            print("Try guessing a lower number.")
        user_guess = ask_input()

    if my_number == user_guess:
        print(f"You guessed it right! \n")    

if __name__ == "__main__":

    #0 if want super hints (additional option ko lng for practice)  
    print("\nTry to guess my special number (Clue: 0-100). Don't worry I'll give you more hints along the way!")
    super_hint_var = super_hint()

    #1 ask user guess with validity check
    user_guess = ask_input()

    #2 generate a random number (0-100)
    my_number = random.randint(0, 100)

    #3 give hints until random number is guessed
    hints(user_guess, my_number, super_hint_var)


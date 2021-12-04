"""ASS8 PROG1
Program 1: Lottery
Create a program that ask 3 numbers (0-9) from the user.
Generate 3 random winning numbers (0-9)
Display “Winner” if all 3 input numbers matched the generated numbers
Display ”You loss” if not
Display ”Try again y/n” after each game
If the user enter “y” the user will play again
if “n” the program will exit."""

#Ass8 Prog1, 1st try,   tried following pep8 naming conventions, finished try again opt pero wala pang random draw, winner/loser, not fully working

import random
import sys

def number_func():
    first_mark = input("\nYour first number:  ")
    second_mark = input("Your second number:  ")
    third_mark = input("Your third number:  ")
    return first_mark, second_mark, third_mark

def check_valid(first_mark, second_mark, third_mark):
    
    while  not first_mark.isdigit() or not second_mark.isdigit() or not third_mark.isdigit(): 
        print("\nPlease only enter numbers from 0-9.")
        try_again()

def try_again():
    while True:
        y_or_n = input("\nWould you like to try again? (Type 'y' for yes and 'n' for no) \n")
        if y_or_n[0] == "y":
            number_func()
        elif   y_or_n[0] == "n":
            print("\nThe program is closing. Thank you for trying!! \n")
            sys.exit()
      

# def lotto_draw():


if __name__ == "__main__":

    #1 Ask 3 numbers and generate 3 random num 
    print("\nWelcome to the Lotto!! \nWe will draw 3 numbers from 0-9 ,and if you match all 3 then congratulations!!")
    first_mark_G, second_mark_G, third_mark_G = number_func()

    #2 Check if valid
    check_valid(first_mark_G, second_mark_G, third_mark_G)

    #3 Determine if winner or loser

    #3 Try again option
    try_again()

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
#            2nd try,   should be working

import random
import sys

def number_func():
    first_mark = input("\nYour first number:  ")
    second_mark = input("Your second number:  ")
    third_mark = input("Your third number:  ")

    user_lotto_mark = [first_mark, second_mark, third_mark]
    user_lotto_mark.sort()

    return first_mark, second_mark, third_mark, user_lotto_mark

def check_valid(first_mark, second_mark, third_mark, user_lotto_mark):
    
    while  not first_mark.isdigit() or not second_mark.isdigit() or not third_mark.isdigit(): 
        print("\nPlease only enter integers from 0-9.")
        try_again()

    for number in user_lotto_mark:
        while int(number) < 0 or int(number) > 9:
            print("\nPlease only enter numbers from 0-9.")
            try_again()


def lotto_result(user_lotto_mark):
    user_lotto_mark = [int(number) for number in  user_lotto_mark]

    first_draw = random.randint(0,9)
    second_draw = random.randint(0,9)
    third_draw = random.randint(0,9)
  
    lotto_winning_draw = [first_draw, second_draw, third_draw]
    lotto_winning_draw.sort()

    print(f"\nThe winning draws are: {first_draw, second_draw, third_draw}")
    if  user_lotto_mark == lotto_winning_draw:
        print("Winner!! Congratulations for winning the lottery!!")
    else:
        print("Sorry, you loss! Don't be sad, the the odds of winning is low anyway.")

def try_again():
    while True:
        y_or_n = input("\nWould you like to try again? (Type 'y' for yes and 'n' for no) \n")

        if y_or_n[0] == "y":
            first_mark, second_mark, third_mark, user_lotto_mark  = number_func()
            check_valid(first_mark, second_mark, third_mark, user_lotto_mark)
            lotto_result(user_lotto_mark)

        elif   y_or_n[0] == "n":
            print("\nThe program is closing. Thank you for trying!! \n")
            sys.exit()

        else:
            print("The program is closing. Next time follow the instructions.\n")
            sys.exit()


if __name__ == "__main__":

    #1 Ask 3 numbers 
    print("\nWelcome to the Lotto!! \nWe will draw 3 numbers from 0-9 ,and if you match all 3 regardless of the order then You are the jackpot winner!!")
    first_mark, second_mark, third_mark, user_lotto_mark = number_func()

    #2 Check if valid
    check_valid(first_mark, second_mark, third_mark, user_lotto_mark)

    #3 Draw the winning numbers and determine if winner or loser
    lotto_result(user_lotto_mark)

    #4 Try again option
    try_again()
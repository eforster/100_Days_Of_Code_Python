"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 4 : Rock, Paper, Scissors

Random module will role for the computer opponent, inputs 0 for rock, 1 for paper, 2 for scissors

Date : 17/12/2022
Author : E Forster

"""

import random

print("Welcome to Rock, Paper, Scissors! \n")
player_choice = int(input("Please choose 0 for rock, 1 for paper, and 2 for scissors :\n"))

# Conditionals and assignments for numbers to actions
if player_choice == 0 :

    print("\nPlayer chose rock. \n")

elif player_choice == 1 :

    print("\nPlayer chose paper. \n")

elif player_choice == 2 :

    print("\nPlayer chose scissors. \n")

else :

    print("\nInvalid input.  Try again. \n")


computer_choice = random.randint(0, 2)              # Computer randomly rolls a number for it's choice of action

if computer_choice == 0 :

    print("Computer chose rock. \n")

elif computer_choice == 1 :

    print("Computer chose paper. \n")

else :

    print("Computer chose scissors. \n")

# Conditions for comparing computer to player choice, to determine win or lose

if computer_choice > player_choice :

    print("Computer wins! \n")

elif player_choice == 0 and computer_choice == 2 :

    print("You win! \n")

elif player_choice > computer_choice :

    print("You win! \n")

else :

    print("It's a draw.\n")

"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 4 : Heads or Tails?

Given a choice of heads or tails, will return a random roll for heads or tails.

Date : 17/12/2022
Author : E Forster

"""

import random

choice = input("Heads or tails? \n")

# Randomly rolls for 0 or 1

roll = random.randint(0, 1)

# Conditions and assignments of numbers for heads or tails

if choice == 'Heads' or choice == 'heads' :

    choice_number = 0

elif choice == 'Tails' or choice == 'tails' :

    choice_number = 1

# Condition for win or lose - does the input match computer roll

if roll == choice_number :

    print(f"You win.  {choice}. \n")

else :

    print(f"You lose. \n")

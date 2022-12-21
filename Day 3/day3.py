"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 3 : Treasure Island

Given choices, player can make decisions to try and reach the treasure.

Date : 15/12/2022
Author : E Forster

"""

print("Welcome to Treasure Island!\n")
print("Your mission is to find the treasure.\n")

choice1 = input("You are at a crossroads.  Do you go left or right? \n").lower()

# Conditions and followings for each step towards treasure.  It is a bit random.

if choice1 == "left" :

    choice2 = input("You follow the fork to the left.  You approach a fast running river.  Do you go back, make a raft or swim for it?  PLease input either back, raft or swim respectively.\n").lower()

    if choice2 == "back" :

        print("You turn back and are immediately shot down with a nuclear missile.  Game over. \n")

    elif choice2 == 'raft' :

        choice3 = input("You successfully build a raft and make it across the river.  You continue onwards and find yourself at another crossroads.  Left or right?\n")

        if choice3 == "left" :

            print("You turn to the fork on the left.  You are abducted by aliens.  Game over.\n")

        else :
            print("You stumble across a giant treasure chest.  You win!\n")

    else :
        print("You are eaten by crocodiles wearing crocs.  You die a painful death.  Game over. \n")

else :
    print("You follow the fork to the right.  You are soon lost and get kidnapped by rats.  You are now the rat king.  Game over?\n")
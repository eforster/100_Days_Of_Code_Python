"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 7 : Hangman 1

Randomly chooses a word from a list, asks the user to guess a letter and make it lowercase, checks if this letter is in the chosen word.

Date : 23/12/2022
Author : E Forster

"""

import random 

# Word list computer can pick from :

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Please guess a letter : \n").lower()
print("Computer will print True or False for every letter in word from the guessed letter. \n")

# For loop to go through each letter in chosen word and compare it to the user's guess letter :

for letter in chosen_word :

    if letter == guess :

        print("True.")

    else :

        print("False.")

"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 7 : Hangman 4

Randomly chooses a word from a list and allocates a underscore per letter to be guessed, asks the user to guess a letter and make it lowercase, 
print if letter is in the word and replace the blanks.  A while loop allows the player to keep guessing until the player has lost all their lives.

Date : 29/12/2022
Author : E Forster

"""

import random 

# Word list computer can pick from, choosing randomly :

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Creates empty list for display :

display = []

# Creates display replacing the letters in the chosen work with '_' :

for i in chosen_word :

    display += '_'

# Creates variables to acknowledge the end of the game and player lives :

end_game = False
player_lives = 6

print(f"You have {player_lives} lives. \n")

# Loop to allow for repeated guesses :

while not end_game :

    guess = input("Please guess a letter : \n").lower()

    # For loop to go through each letter in chosen word and compare it to the user's guess letter :

    for letter_position in range(len(chosen_word)) :

        # Gives placement within the chosen_word to loop through to amend if the player guesses correctly

        letter = chosen_word[letter_position]

        # Conditional for if the letter matches the guess, filling in the blank

        if letter == guess :
            
            display[letter_position] = letter

    # Conditions for when player guesses incorrectly :

    if letter != guess :

        player_lives = player_lives - 1
        print(f"You have {player_lives} lives remaining. \n")

        # Condition for when player's lives reaches zero.

        if player_lives == 0 :

            end_game = True
            print("Out of lives.  You lose. \n")


    # Prints the display for the turn

    print(display, "\n")

    # Condition for the player to win, if all the '_'s are gone :

    if '_' not in display :

        end_game = True
        print(f"You win.  Word was : {chosen_word}. \n")
        
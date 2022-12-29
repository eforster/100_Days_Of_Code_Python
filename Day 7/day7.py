"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 7 : Hangman 5 Final

Randomly chooses a word from a list and allocates a underscore per letter to be guessed, asks the user to guess a letter and make it lowercase, 
print if letter is in the word and replace the blanks.  A while loop allows the player to keep guessing until the player has lost all their lives.

Date : 29/12/2022
Author : E Forster

"""

import random 

# Imports artwork for hangman game :

from hangman_art import logo, stages

# Imports a word list from another file :

from hangman_words import word_list

# Word list computer can pick from, choosing randomly :

chosen_word = random.choice(word_list)

# Creates empty list for display :

display = []

# Creates display replacing the letters in the chosen work with '_' :

for i in chosen_word :

    display += '_'

# Creates variables to acknowledge the end of the game and player lives :

end_game = False
player_lives = 6

print(logo, "\n")

print(f"You have {player_lives} lives. \n")
print(stages[player_lives], "\n")

# Loop to allow for repeated guesses :

while not end_game :

    print("\n")
    guess = input("Please guess a letter : \n").lower()
    print("\n")

    if guess in display :

        print(f"You have already guessed {guess}. \n")

    # For loop to go through each letter in chosen word and compare it to the user's guess letter :

    for letter_position in range(len(chosen_word)) :

        # Gives placement within the chosen_word to loop through to amend if the player guesses correctly

        letter = chosen_word[letter_position]

        # Conditional for if the letter matches the guess, filling in the blank

        if letter == guess :
            
            display[letter_position] = letter


    # Conditions for when player guesses incorrectly :

    if guess not in chosen_word :

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        player_lives = player_lives - 1
        print(f"You have {player_lives} lives remaining. \n")
        
        # Condition for when player's lives reaches zero.

        if player_lives == 0 :

            end_game = True
            print("Out of lives.  You lose. \n")
            print(f"Word was {chosen_word}. \n")

    # Prints the display for the turn as well as the hangman stage dependent on player's lives :

    print(stages[player_lives], "\n")

    print(f"{' '.join(display)} \n")

    # Condition for the player to win, if all the '_'s are gone :

    if '_' not in display :

        end_game = True
        print(f"You win.  Word was : {chosen_word}. \n")
        
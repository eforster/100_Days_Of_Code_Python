"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 8 : Caesar Cipher

Angela has split this into 4 separate files but I will condense into one.

The purpose of this file is to take user input of text and given user choice of encrypt or decrypt, and does so. 

Date : 12/01/2023
Author : E Forster

"""

# Creates a library for the alphabet

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, input_text, text_shift) :

    caesar_text = ""                                    # Empty string to be added to later as function works

    if direction == "decode" :
                                                        # Condition for decoding which menas the caesar cipher works in reverse, requiring a negative
        text_shift *= -1

    for char in input_text :
                                                            # Loops through each character in input text and amends it to encode or decode, adding to final message, ignoring numbers and symbols
        if char in alphabet :

            initial_position = alphabet.index(char)
            position = (initial_position + shift) % 26          # Allows for shift number higher than 26, length of the alphabet list
            caesar_text += alphabet[position]

        else :

            caesar_text += char

    print(f"The {direction}d text is : {caesar_text}. \n")    

user_continue = True      # Condition to be finished using the cipher

while user_continue :

    # Takes user inputs for encoding or decoding, message to be manipulated and the shift number, relevant to Caesar Cipher :

    direction = input("Type 'encode' to encrypt or 'decode' to decrypt :\n")
    text = input("Type your message :\n").lower()
    shift = int(input("Type the shift number :\n"))

    caesar(direction, text, shift)

    restart = input("Type 'yes' to go again.  Otherwise, type 'no' : \n")           # Condition to go again

    if restart == 'no' :

        user_continue == False
        print("Thank you for using Caesar Cipher. \n")
        quit()


"""

# Encode and Decrypt as separate functions for Part 1 and 2 of Day 8.  This is what was condensed in the above caesar function :

def encrypt(input_text, text_shift) :

    encrypted_text = ""                                        # Creates empty string to be added to as encode works

    for char in input_text :                                # Loops through each character in the input text

        initial_position = alphabet.index(char)             # Finds a character's input_text in the alphabet and takes note of that index
        new_position = initial_position + text_shift        # Changes the index by the shift amount

        if new_position > len(alphabet) - 1 :               # Condition to prevent IndexError

            new_position = new_position - len(alphabet)     # Sets new position index

        encrypted_text += alphabet[new_position]               # Adds new letter to encode text by tracing that index to alphabet

    print(f"The encoded text is {encrypted_text}. \n")


def decrypt(input_text, text_shift) :

    decoded_text = ""                                       # Creates empty string to be added to as decode works

    for char in input_text :                                # Loops through each character in input text

        initial_position = alphabet.index(char)             # Finds a character's input_text in the alphabet and takes note of that index
        new_position = initial_position - text_shift        # Changes the index by the shift amount

        if new_position > len(alphabet) - 1 :               # Condition to prevent IndexError

            new_position = new_position - len(alphabet)     # Sets new position index

        decoded_text += alphabet[new_position]              # Adds new letter to decode text by tracing that index to alphabet

    print(f"The encoded text is {decoded_text}. \n")
"""
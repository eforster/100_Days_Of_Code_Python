"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 5 : PyPassword Generator

Taking in an input of quantity of letters, numbers and symbols, returns a new possible password.

Date : 21/12/2022
Author : E Forster

"""

import random as random

print("Welcome to the PyPassword Generator.\n")

# Takes desired inputs for implementation later

letter_choice = int(input("How many letters would you like?\n"))
symbol_choice = int(input("How many symbols would you like?\n"))
number_choice = int(input("How many numbers would you like?\n"))

# Creates library for letters, symbols and numbers that can be used in passwords.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '(', ')', '*', '+']

# Uses random.sample to select randomly from the libraries according to user choice

random_letters = random.sample(letters, letter_choice)
random_symbols = random.sample(symbols, symbol_choice)
random_numbers = random.sample(numbers, number_choice)

# Strings together the random computer choices

string = random_letters + random_symbols + random_numbers

# Shuffles the string to randomly generate your password, joins to a string so it doesn't print as a list

randomised_string = random.sample(string, len(string))
password = ''.join(randomised_string)

print(f"Your new password is : {password}\n")

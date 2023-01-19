"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 8 : Prime Number Checker

Creates a function called prime_checker that takes a user inputted number and checks if it is prime.

Date last edited : 06/01/2023
Author : E Forster

"""

import math

# Defines function for checking if a number is prime, aka only divisible by itself and 1 :

def prime_checker(number) :
    
    # Assumes prime property is true :

    is_prime = True

    # Loop to check all numbers from 2 to itself, if perfectly divisible by any of these, it is not a prime number

    for i in range(2, number) :

        if number % i == 0 :

            is_prime = False

# If number has been assigned is_prime to be true, prints to terminal that the number is prime :

    if is_prime :

        print("Number is prime. \n")

    else :

        print("Number is not prime. \n")

# Takes a number from user input then checks it using prime_checker function :

n = int(input("Check this number : \n"))
prime_checker(n)
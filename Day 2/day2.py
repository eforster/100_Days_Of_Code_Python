"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 2 : Tip Calculator 

When given the total bill, percentage tip and number of people, this calculator returns the amount per person to be paid.

Date : 14/12/2022
Author : E Forster

"""

print("Welcome to Tip Calculator. \n")

total = float(input("What was the total bill? £"))                                  # Takes total bill as input
percentage = int(input("What percentage tip would you like to give? \n"))           # Takes a percentage as input for tip
num_people = int(input("How many people to split the bill? \n"))                    # Takes in number of people to split bill between

# Percentage divided by 100 gives tip as decimal value, adds 1 to make it a percentage increase which can then be used to divide equally among the people
person_pay = round((total * ((percentage / 100) + 1)) / num_people, 2)

print("Each person should pay : £", person_pay)

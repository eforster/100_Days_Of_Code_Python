"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 2 : Tip Calculator

Date : 12/12/2022
Author : E Forster

"""

print("Welcome to Tip Calculator. \n")

total = float(input("What was the total bill? £"))
percentage = int(input("What percentage tip would you like to give? \n"))
num_people = int(input("How many people to split the bill? \n"))

# Percentage divided by 100 gives tip as decimal value, adds 1 to make it a percentage increase which can then be used to divide equally among the people
person_pay = round((total * ((percentage / 100) + 1)) / num_people, 2)

print("Each person should pay : £", person_pay)

"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 5 : Even Numbers

Sums all the even numbers from 1 to 100.

Date : 21/12/2022
Author : E Forster

"""

# Initialises total

total = 0

for number in range(0, 101) :

    if number % 2 == 0 :        # Condition for an even number

        total += number         # Adds even numbers to total

print("Total is : ", total)

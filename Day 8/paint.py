"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 8 : Paint Area Calculator

Creates a function called area that calculates the total area to be painted, 
then uses this function to work out how many cans of paint are needed in coverage of 5 square metres of wall per can.

Date : 06/01/2023
Author : E Forster

"""

import math

# Function to calculate number of cans needed for full coverage on desired wall given wall parameters :

def calculate_paint(height, width, coverage) :

    area = width * height
    number_cans = area / coverage
    return number_cans

# Takes user inputs for desired wall parameters :

wall_height = int(input("Wall height (metres) : \n"))
wall_width = int(input("Wall width (metres) : \n"))
coverage = 5

# Calls function using user input :

cans = (calculate_paint(wall_height, wall_width, coverage))
cans = round(cans, 0)
print(f"Number of cans needed : {cans}. \n")

"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 4 : Banker Roulette : Who will pay the dinner bill?

Given a list of names, will return a name from list at random to determine who pays the bill.

Date : 17/12/2022
Author : E Forster

"""

import random

names = input("Please input the names of everyone that is participating in Banker Roulette in the following format : Bob, Sandy, etc : \n")

name_list = names.split(",")

roulette = random.randint(0, len(name_list) - 1)

print(f"{name_list[roulette]} will pay the bill. \n")

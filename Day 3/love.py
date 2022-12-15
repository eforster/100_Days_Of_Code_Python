"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 3 : Love Calculator

Date : 15/12/2022
Author : E Forster

"""

print("Welcome to the Love Calculator.\n")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

# Initialises love_score for adding later, combines input names to one string and makes it all lower case.

love_score = 0
names = name1 + name2
string = names.lower()

l = string.count("l")
o = string.count("o")
v = string.count("v")
e = string.count("e")

t = string.count("t")
r = string.count("r")
u = string.count("u")
e = string.count("e")


love = l + o + v + e
true = t + r + u + e

love_score = int(str(true)) + int(str(true))

if love_score < 10 or love_score > 90 :

    print("Your score is : ", love_score, ", you go together like coke and mentos.\n")

elif 40 >= love_score >= 50 :

    print("Your score is :", love_score, ", you are alright together. \n")

else :

    print("Your love score is :", love_score)
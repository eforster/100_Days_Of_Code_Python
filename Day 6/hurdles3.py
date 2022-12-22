"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 6 : Hurdles 3 with Reeborg's World

Program for Reeborg to look ahead, jump any hurdles and not hit them.

Reeborg has a small library of funtions and special features that the user can add to to beat challenges.

See README.md for details where this code can be used.

Date : 22/12/2022
Author : E Forster

"""

# Function to turn right instead of only left :

def turn_right() :

    turn_left()
    turn_left()
    turn_left()


# Function to jump a hurdle :

def jump() :

    turn_left() 
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Tells robot to do movements until they reach the goal :

while not at_goal() :

    if front_is_clear() :
        
        move()
        
    else :
        
        jump()

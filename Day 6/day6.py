"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 6 : Escape the Maze with Reeborg's World

Program for Reeborg to escape a maze by keeping walls on his right to keep to the edges as much as possible

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


# Tells robot to do certain movements until the goal is reached :

# First loop to move when front is clear :

while front_is_clear() :
    
    move()
    
# Until can no longer go forward, then turn left :

turn_left()

# Second loop to ensure ability to continue until goal is reached :
    
while not at_goal() :

    # Nested if-elif-else loops for different scenarios, keeping Reeborg to the walls with a wall on his right, moving around the board along the edges.
    
    if right_is_clear() :
        
        turn_right()
        move()
        
    elif front_is_clear() :
    
        move()
        
    else :
        
        turn_left()

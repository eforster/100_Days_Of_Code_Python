"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 4 : Treasure Map

Using horizontal rows and vertical columns respectively (for examples, 20 would be row 2 and column 0), user can guess where the treasure has been placed using the random module.

Date : 17/12/2022
Author : E Forster

"""

import random

print("Welcome to Treasure Hunt!\n")
print("Below is a map of possible positions the treasure could be. \n")

row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
map = [row0, row1, row2]
print(f"{row0}\n{row1}\n{row2}\n")

treasure_x = random.randint(0, 2)
treasure_y = random.randint(0, 2)
treasure = str(treasure_x) + str(treasure_y)

guess1 = input("Please input from 0-2 a row number and a column number for your first guess of where the treasure is :\n")

if guess1 == treasure :

    print("Congratulations!  You have found the treasure. X marks the spot!\n")
    row = int(treasure_x)
    column = int(treasure_y)
    map[row][column] = 'X'
    print(f"{row0}\n{row1}\n{row2}\n")


else :

    row = int(guess1[0])
    column = int(guess1[1])
    map[row][column] = "O"

    print("Unlucky!  Try again? \n")
    print("Updated map : \n")
    print(f"{row0}\n{row1}\n{row2}\n")

    guess2 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")
    

    if guess2 == treasure :

        print("Congratulations!  You have found the treasure. X marks the spot!\n")
        row = int(treasure_x)
        column = int(treasure_y)
        map[row][column] = 'X'
        print(f"{row0}\n{row1}\n{row2}\n")

    else :

        row = int(guess2[0])
        column = int(guess2[1])
        map[row][column] = "O"

        print("Unlucky!  Try again? \n")
        print("Updated map : \n")
        print(f"{row0}\n{row1}\n{row2}\n")

        guess3 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")


        if guess3 == treasure :

            print("Congratulations!  You have found the treasure. X marks the spot!\n")
            row = int(treasure_x)
            column = int(treasure_y)
            map[row][column] = 'X'
            print(f"{row0}\n{row1}\n{row2}\n")

        else :

            row = int(guess3[0])
            column = int(guess3[1])
            map[row][column] = "O"

            print("Unlucky!  Try again? \n")
            print("Updated map : \n")
            print(f"{row0}\n{row1}\n{row2}\n")

            guess4 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

            if guess4 == treasure :

                print("Congratulations!  You have found the treasure. X marks the spot!\n")
                row = int(treasure_x)
                column = int(treasure_y)
                map[row][column] = 'X'
                print(f"{row0}\n{row1}\n{row2}\n")

            else :

                row = int(guess4[0])
                column = int(guess4[1])
                map[row][column] = "O"

                print("Unlucky!  Try again? \n")
                print("Updated map : \n")
                print(f"{row0}\n{row1}\n{row2}\n")

                guess5 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

                if guess5 == treasure :

                    print("Congratulations!  You have found the treasure. X marks the spot!\n")
                    row = int(treasure_x)
                    column = int(treasure_y)
                    map[row][column] = 'X'
                    print(f"{row0}\n{row1}\n{row2}\n")

                else :

                    row = int(guess5[0])
                    column = int(guess5[1])
                    map[row][column] = "O"

                    print("Unlucky!  Try again? \n")
                    print("Updated map : \n")
                    print(f"{row0}\n{row1}\n{row2}\n")

                    guess6 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

                    if guess6 == treasure :

                        print("Congratulations!  You have found the treasure. X marks the spot!\n")
                        row = int(treasure_x)
                        column = int(treasure_y)
                        map[row][column] = 'X'
                        print(f"{row0}\n{row1}\n{row2}\n")

                    else :

                        row = int(guess6[0])
                        column = int(guess6[1])
                        map[row][column] = "O"

                        print("Unlucky!  Try again? \n")
                        print("Updated map : \n")
                        print(f"{row0}\n{row1}\n{row2}\n")

                        guess7 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

                        if guess7 == treasure :

                            print("Congratulations!  You have found the treasure. X marks the spot!\n")
                            row = int(treasure_x)
                            column = int(treasure_y)
                            map[row][column] = 'X'
                            print(f"{row0}\n{row1}\n{row2}\n")  

                        else :

                            row = int(guess7[0])
                            column = int(guess7[1])
                            map[row][column] = "O"

                            print("Unlucky!  Try again? \n")
                            print("Updated map : \n")
                            print(f"{row0}\n{row1}\n{row2}\n")

                            guess8 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

                            if guess8 == treasure :

                                print("Congratulations!  You have found the treasure. X marks the spot!\n")
                                row = int(treasure_x)
                                column = int(treasure_y)
                                map[row][column] = 'X'
                                print(f"{row0}\n{row1}\n{row2}\n")  

                            else :

                                row = int(guess8[0])
                                column = int(guess8[1])
                                map[row][column] = "O"

                                print("Updated map : \n")
                                print(f"{row0}\n{row1}\n{row2}\n")

                                guess9 = input("Please input from 0-2 a row number and a column number for another guess of where the treasure is :\n")

                                if guess9 == treasure :

                                    print("Congratulations!  You have found the treasure. X marks the spot!\n")
                                    row = int(treasure_x)
                                    column = int(treasure_y)
                                    map[row][column] = 'X'
                                    print(f"{row0}\n{row1}\n{row2}\n")  
                                    
                                else :

                                    print("Unlucky.  Here is the treasure location, X marks the spot. \n")
                                    row = int(treasure_x)
                                    column = int(treasure_y)
                                    map[row][column] = 'X'
                                    print(f"{row0}\n{row1}\n{row2}\n")                   
                                
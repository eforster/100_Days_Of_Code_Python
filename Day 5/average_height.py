"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 5 : Average Height Calculator

Without using library functions, calculator takes in a list of heights and calculates the average height.

Date : 18/12/2022
Author : E Forster

"""

height_list = input("Please input a list of heights : \n").split(",")

for i in range(0, len(height_list)) :

    height_list[i] = int(float(height_list[i]))

total_height  = 0

for height in height_list :

    total_height += height
    
average_height = total_height / len(height_list)

print(f"Average height is : {average_height} cm. \n")

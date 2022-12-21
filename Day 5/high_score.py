"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 5 : High Score

Without using library functions, calculator takes in a list of scores and returns the highest score.

Date : 21/12/2022
Author : E Forster

"""

student_scores = input("Input a list of scores : \n").split(",")

high_score = 0                      # Initialises high_score to add to later

for i in range(0, len(student_scores)) :

    student_scores[i] = int(float(student_scores[i]))

for score in student_scores :

    if score > high_score :         # Iterates through list, if score in student_scores is greater than 0, sets that as high score and continues comparing until the highest score is found

        high_score = score
            
print(f"The highest score is : {high_score}.\n")           

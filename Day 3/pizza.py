"""

100 Days of Code : The Complete Python Pro Bootcamp by Dr. Angela Yu on Udemy

Day 3 : Pizza Delivery

When given a pizza size and topping options, this calculates the total cost.

Date : 15/12/2022
Author : E Forster

"""

print("Welcome to Python Pizza Deliveries! \n")
size = input("What size pizza would you like?  Please choose from : S, M or L \n")
add_pepperoni = input("Would you like pepperoni?  Y for Yes and N for No : \n")
extra_cheese = input("Would you like extra cheese?  Y for Yes and N for No : \n")

# Pricings for pizza sizes and toppings :

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni = 3
cheese = 1

# Initialised final_bill to be added to later :

final_bill = 0

if size == 'S' or size == 's' :
     
     final_bill += small_pizza

     if add_pepperoni == 'Y' or add_pepperoni == 'y' :

        final_bill += pepperoni_small

        if extra_cheese == 'Y' or extra_cheese == 'y' :

            final_bill += cheese

        else :
            pass
     else :
        pass

elif size == 'M' or size == 'm' :

    final_bill += medium_pizza

    if add_pepperoni == 'Y' or add_pepperoni == 'y' :

        final_bill += pepperoni

        if extra_cheese == 'Y' or extra_cheese == 'y' :

            final_bill += cheese

        else :
            pass
    else :
        pass

elif size == 'L' or size == 'l' :

    final_bill += large_pizza 

    if add_pepperoni == 'Y' or add_pepperoni == 'y' :

        final_bill += pepperoni

        if extra_cheese == 'Y' or extra_cheese == 'y' :

            final_bill += cheese

        else :
            pass
    else :
        pass

else :
    
    print("Input error. \n")


print("Your final bill is : £", round(final_bill, 2))
#! /usr/bin/python
# Exercise No.   1
# File Name:     MyFirstProgram.py
# Programmer:    John Rollinson
# Date:          8/28/2019
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of 
# these three numbers and the product, and display the sum and product to the screen.
#
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Calculate the product of the integers
# 5. Print the sum of the integers to the screen
# 6. Print the product of the integers to the screen
#
# import the necessary python libraries
# for this example none are needed


def main():
    # Print a message to the screen
    print("Hello!")
    print("I can add and multiply three numbers for you")

    # Variables are declared dynamically no need to pre-define
    num1 = eval(input("Enter a whole number(Ex. 52):"))
    num2 = eval(input("Enter a second whole number(Ex. 41):"))
    num3 = eval(input("Enter a third whole number(Ex. 22):"))

    percentage = (num1 / num2 ) * 100
    print("Percentage = ", percentage)

    #Here is the processing that is needed
    sum = num1 + num2 + num3
    product = num1 * num2 * num3

    # Output the results
    print("The sum of the three numbers is", sum)
    print("The product of the three numbers is", product)

main()

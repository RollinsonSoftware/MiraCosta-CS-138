#! /usr/bin/python
# Exercise No.   01
# File Name:     hw8project1.py
# Programmer:    John Rollinson
# Date:          10/20/2019
#
# Problem Statement:
# Write a program that computes and outputs the nth Fibonacci number, where n is
# is a value entered by the user.
#
# Overall Plan:
# 1. Define the fibonacci function with n as the parameter.
# 2. Initialize the base case as 1 and define the case for the first and second terms.   
# 3. Run a loop from the second term to the nth term.
# 4. Each iteration should find the next term while also saving the last two terms.
# 5. Ask user to enter the position to find desired value.
# 6. Print the desired value. 
#
# import the necessary python libraries
def fibonacci(n):
    a = 1
    b = 1
    if(n < 0):
        print("Incorrect input.")
    elif(n == 0):
        return(a)
    elif(n == 1):
        return(b)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return(b)

def main():
    print("This program will find the desired term of the fibonacci sequence!")

    n = int(input("Enter the nth term of the sequence: "))
    print("The fibonacci number is:", fibonacci(n))

main()
        

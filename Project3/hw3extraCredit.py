#! /usr/bin/python
#Exercise No.  Extra Credit
#File Name:    hw3extraCredit.py
#Programmer:   John Rollinson
#Date: 9/6/2019
#
#Problem Statement: (what you want the code to do)
#Divides two numbers and outputs the results using whole numbers and the remainder.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Read in as input two whole numbers from the user.
#2. Calculate what the quotient is using integer division.
#3. Calculate the remainder using the modular operator. 
#4. Output the results to the user. 
#
#import necessary python libraries
#Create main function
def main():
    print("Divides two numbers and outputs the results using whole numbers and the remainder.")
    
    first = eval(input("Enter the first whole number: "))
    second = eval(input("Enter the second whole number: "))

    quotient = first // second
    remainder = first % second

    print(first, "divided by", second, "is equal to:", quotient, "remainder", remainder)
    
main()

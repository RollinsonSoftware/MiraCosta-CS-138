#! /usr/bin/python
# Exercise No.   02
# File Name:     hw6project2.py
# Programmer:    John Rollinson
# Date:          9/29/2019
#
# Problem Statement:
# Write a program that includes a function that takes a list of numbers as
# input and returns the sum of all the numbers in the list.
#
# Overall Plan:
# 1. Initialize the sum to zero before the for loop.
# 2. Iterate through the numbers in the list and add them to the sum and
#       return the sum of the numbers.
# 3. Define a main function to test the method. 
#
# import the necessary python libraries
def sumList(myList):
    sum = 0

    for number in myList:
        sum += number

    return(sum)

def main():
    list = [1, 2, 4, 5, 7]
    
    print("This is the original list: ", list)
    print("The sum of the numbers in the list is: ", sumList(list))

main()


          

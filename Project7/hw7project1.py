#! /usr/bin/python
# Exercise No.   01
# File Name:     hw7project1.py
# Programmer:    John Rollinson
# Date:          10/06/2019
#
# Problem Statement:
# Write a program that calculates and prints your grade. Input is the percentage
# of points that you received, the output is the letter grade. Your code should
# handle all percentage points in the grading scale. Use the grading scale for
# this class. 
#
# Overall Plan:
# 1. Show the current grading scale to the user, and prompt them to enter their
#       grade as a percentage.
# 2. Use branching statements to determine what their letter grade is.   
# 3. Output the letter grade to the console for the user to see.
#
# import the necessary python libraries
def main():
    print("The current grading scale is as follows:\n90%-100% = A\n80%-89.99% = B\n70%-79.99% = C\n60%-69.99% = D\n0%-59.99% = F")

    percentage = float(input("Enter your current percentage in the class: "))

    if percentage <= 100 and percentage >= 90:
        print("Your current grade: A")
    elif percentage < 90 and percentage >= 80:
        print("Your current grade: B")
    elif percentage < 80 and percentage >= 70:
        print("Your current grade: C")
    elif percentage < 70 and percentage >= 60:
        print("Your current grade: D")
    else:
        print("Your current grade: F")
                   
main()

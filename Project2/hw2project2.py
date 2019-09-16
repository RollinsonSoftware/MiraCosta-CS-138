#! /usr/bin/python
#Exercise No.  02
#File Name:    hw2project2.py
#Programmer:   John Rollinson
#Date: 8/31/2019
#
#Problem Statement: (what you want the code to do)
#A program to convert Fahrenheit temps to Celsius.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Describe what the program does to the user with a print statement.
#2. Read in a Fahrenheit value from the user.
#3. Convert the temp to Celsius.
#4. Print out the converted value to the user.
#
#import necessary python libraries
#Create main function

def main():
    print("This program will convert a temperature given in Fahrenheit to Celsius!")
    
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5 * (fahrenheit - 32) / 9
    print("The temperature is", celsius, "degrees Celsius.")

main()

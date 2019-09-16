#! /usr/bin/python
#Exercise No.  01
#File Name:    hw2project1.py
#Programmer:   John Rollinson
#Date: 8/31/2019
#
#Problem Statement: (what you want the code to do)
#A program to convert Celsius temps to Fahrenheit.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Describe what the program does to the user with a print statement.
#2. Read in a celsius value from the user.
#3. Convert the temp to Fahrenheit.
#4. print out the converted value to the user.
#
#import necessary python libraries
#Create main function

def main():
    print("This program will convert a temperature given in Celsius to Fahrenheit!")
    
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

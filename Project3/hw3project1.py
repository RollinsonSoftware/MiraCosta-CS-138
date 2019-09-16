#! /usr/bin/python
#Exercise No.  01
#File Name:    hw3project1.py
#Programmer:   John Rollinson
#Date: 9/6/2019
#
#Problem Statement: (what you want the code to do)
#Calculates the cost per square inch of a circular pizza,
#given its diameter and price. 
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Get the size of the pizza's diameter fromt he user in inches.
#2. Get the total cost of the pizza from the user. 
#3. Calculate the area of the pizza, make sure to use the radius (half the diameter).
#4. Calculate the cost per square inch of pizza (cost / square inches)
#5. Output the total cost per square inch to the user. 
#
#import necessary python libraries
#Create main function
import math

def main():
    print("This program Calculates the cost per square inch of a circular pizza, given its diameter and price.")
    diameter = eval(input("Enter the diameter of the pizza (in inches): "))
    cost = eval(input("Enter the price of the pizza: $"))

    area = math.pi * ((diameter / 2) ** 2)

    costPerSquareInch = cost / area

    print("The cost per square inch of pizza is: $", costPerSquareInch)

main()

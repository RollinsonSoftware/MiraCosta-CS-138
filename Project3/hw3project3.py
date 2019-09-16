#! /usr/bin/python
#Exercise No.  03
#File Name:    hw3project3.py
#Programmer:   John Rollinson
#Date: 9/6/2019
#
#Problem Statement: (what you want the code to do)
#Determines the length of a ladder required to reach a given height when leaned
#against a house.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Take in as input from the user, the height of the house and the angle of the ladder. 
#2. Convert the angle from degrees to radians. 
#3. Calculate the length of the ladder needed to reach the top of the house.
#4. Output the result to the user.
#
#import necessary python libraries
#Create main function
import math

def main():
    print("Determines the length of a ladder required to reach a given height when leaned against a house.")
    height = eval(input("Please enter the height of the house (in meters): "))
    angle = eval(input("Please enter the angle of the ladder (in degrees): "))

    #follows order of operations, no need for ()'s
    radians = math.pi / 180 * angle 
    length = height / math.sin(radians)

    print("The ladder will need to be", length, "meters high to reach the top of the house.")
main()    

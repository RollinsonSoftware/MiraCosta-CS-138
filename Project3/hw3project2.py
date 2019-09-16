#! /usr/bin/python
#Exercise No.  02
#File Name:    hw3project2.py
#Programmer:   John Rollinson
#Date: 9/6/2019
#
#Problem Statement: (what you want the code to do)
#Calculates the cost per square inch of a circular pizza,
#given its diameter and price. 
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Prompt the user for any year. 
#2. Divide the year by 100 using integer division. 
#3. Calculate the Gregorian epact. 
#4. Output the result to the user. 
#
#import necessary python libraries
#Create main function

def main():
    print("This program calculates the Gregorian epact, given a certain year.")
    year = eval(input("Please enter a year: "))

    c = year // 100
    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30
    
    print("The Gregorian epact for", year, "is:", epact)

main()

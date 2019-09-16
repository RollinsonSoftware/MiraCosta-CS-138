#! /usr/bin/python
#Exercise No.  03
#File Name:    hw2project3.py
#Programmer:   John Rollinson
#Date: 8/31/2019
#
#Problem Statement: (what you want the code to do)
#A simple program to average N number of exam scores.
#Illustrates use of multiple input.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Read in the number of scores that will need to be averaged.
#2. Keep a total of all the scores with each loop iteration.
#3. Ask user for a test score and add it to the total with each iteration.
#4. Calculate the average and output the result to the user.
#
#import necessary python libraries
#Create main function

def main():
    print("This program computes the average of N number of exam scores.")
    numScores = eval(input("Enter the number of exam scores to be averaged: "))

    scoreTotal = 0
    for i in range(numScores):
        score = eval(input("Enter an exam score: "))
        scoreTotal = scoreTotal + score

    average = scoreTotal / numScores

    print("The average of the scores is:", average)

main()

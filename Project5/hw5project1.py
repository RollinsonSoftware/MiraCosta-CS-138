#! /usr/bin/python
# Exercise No.   01
# File Name:     hw5project1.py
# Programmer:    John Rollinson
# Date:          9/22/2019
#
# Problem Statement:
# Write a program that allows the user to type in a phrase and then outputs
#   the acronym for that phrase. 
#
# Overall Plan:
# 1. Accept the phrase as input from the user.
# 2. Split the words in the given phrase using the split function.
# 3. Convert the intial character of each word using the index position into
# 4.    upper case and store in a string variable. 
# 5. Print the output of the acronym.
#
# import the necessary python libraries
# for this example none are needed

#Define function to determine acronym.
def main():
    print("Acronym Representation!")
    #Read the input from the user.
    phrase = input("Enter the phrase: ")
    acro = ""

    #Use a for loop to split the sentence into separate words. 
    for i in phrase.split():
        #append first character of each character.
        acro = acro + i[0]

    #display acronym on the screen.
    print("Acronym for the given phrase is: ", acro.upper())

main()

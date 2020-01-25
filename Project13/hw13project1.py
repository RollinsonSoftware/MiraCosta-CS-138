#! /usr/bin/python
# Exercise No.   01
# File Name:     hw13project1.py
# Programmer:    John Rollinson
# Date:          11/23/2019
#
# Problem Statement:
# Write a recursive function that detects whether a string is a pallindrome.
# Use the function in a program that prompts the user for a phrase and then
# tells whether or not it is a palindrome. Here's another classic for testing:
# "A man, a plan, a canal, Panama!"
#
# Overall Plan:
# 1. Define a main() function which reads a string from user and then call
#       check_palindrome() function.
# 2. Define the check_palindrome() function to check user entered string is a
#       palindrome or not.
# 3. In check_palindrome() function remove all punctuations from the user entered
#       string.
# 4. Use if-else statements to return true if whole string is traversed by
#       recursively call check_palindrome() function otherwise false.
# 5. At the end in main() function according to return value of check_palindrome()
#       function, display appropriate message.
#
# import the necessary python libraries
import string

def check_palindrome(mystring):
        mystring = "".join([chars.lower() for chars in mystring
                            if chars not in string.punctuation])
        mystring = mystring.replace(" ", "")

        if(len(mystring) == 0 or len(mystring) == 1):
            return(True)
        else:
            return(mystring[0] == mystring[-1] and (check_palindrome(mystring[1:-1])))

def main():
    inp = input("Enter a string: ")
    result = check_palindrome(inp)

    if(result == True):
        print("Yes, it is a palindrome.")
    else:
        print("No, it is not a palindrome.")

main()
            

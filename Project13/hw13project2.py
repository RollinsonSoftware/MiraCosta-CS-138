#! /usr/bin/python
# Exercise No.   02
# File Name:     hw13project2.py
# Programmer:    John Rollinson
# Date:          11/23/2019
#
# Problem Statement:
# Write a program that allows a user to enter a number and a base and then then
# prints out the digits of the number in the new base. Use a recursive function
# baseConversion(num, base) to print the digits.
#
# write a recursive function that first prints the digits of num//base and then
# prints the last digit, namely num%base. You should put a space between successive
# digits, since bases greater than 10 will print out with multi-character digits.
# For example: baseConversion(245, 16) should print 15 5.
#
# Overall Plan:
# 1. Write the baseConversion() function to convert a number into base 16. 
# 2. Use if-else statement to check num is equal to 0 or not.
# 3. If num is not equal to 0 then as suggested reverse the list.
# 4. After this recursively call the same function.
#
# import the necessary python libraries
import string

def baseConversion(num, base, mylist):
    if(num == 0):
        mylist.reverse()
        print(mylist)
    else:
        mylist.append(num % base)
        num = int(num / base)
        baseConversion(num, base, mylist)
        print("{0} in base {1} is: {2}".format(num, base, mylist))

def main():

    baseConversion(245, 2, [])

main()

#! /usr/bin/python
# Exercise No.   2
# File Name:     chaos.py
# Programmer:    John Rollinson
# Date:          8/28/2019
#
# Problem Statement: Chapter 1 Discussion 5 pg.23. Trace through the
# “chaos” program from Section 1.6 by hand using 0.15 as the input value.
# Show the sequence of output that results
#
#
# Overall Plan:
# 1. Read in a double value from the user between 0 and 1.
# 2. Loop this value through the equation "3.9 * x * (x-1)" 10 times.
# 3. Output each iteration of the loop. 
#
# import the necessary python libraries
# for this example none are needed

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

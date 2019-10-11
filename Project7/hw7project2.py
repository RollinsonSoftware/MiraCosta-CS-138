#! /usr/bin/python
# Exercise No.   02
# File Name:     hw7project2.py
# Programmer:    John Rollinson
# Date:          10/06/2019
#
# Problem Statement:
# Write a program that accepts a speed limit and a clock speed and either prints
# a message indicating the speed was legal or prints the amount of the fine, if
# the speed is illegal. $50 + $5 for each mph over the speed limit plus a $200
# penalty for any speed over 90 mph.
#
# Overall Plan:
# 1. Define a function, names speed(), to take the speed limit and clock speed
#       inputs and prints the fine amount.
# 2. Create input variables sl and cs for taking the values of the speed limit
#       and clock speed respectively.
# 3. Save ticket charges in variable ticket.
# 4. If the value of cs is less than or equal to that of sl then prints the
#       message "speed was legal."
# 5. Else if the value of cs is less than or equal to that of sl then calculate the
#       fine as speed over limit (i) multiplied by 5.
# 6. Else if the value of cs is greater than 90 then calculate the fine as the
#       addition of 200 and difference of cs and sl multiplied by 5.
# 7. Print the total amount as ticket plus fine, in case of illegal limit as well
#       as if clock speed is greater than 90 mph.
# import the necessary python libraries
def speed():
    sl = eval(input("Enter speed limit: "))
    cs = eval(input("Enter clock speed: "))
    ticket = 50

    if(cs <= sl):
        print("Speed was legal.")
    else:
        i = cs - sl

        if(cs <= 90):
            fine = i * 5
        else:
            fine = 200 + i * 5

        print("Speed is illegal and the amount of the fine is: $", ticket + fine)

def main():

    speed()

main()

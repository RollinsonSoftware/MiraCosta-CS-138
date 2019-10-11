#! /usr/bin/python
# Exercise No.   01
# File Name:     hw6project1.py
# Programmer:    John Rollinson
# Date:          9/29/2019
#
# Problem Statement:
# Write a program that has two methods in it. One that returns the surface area
# of a sphere having the given radius, and one that returns the volume of a sphere
# having the given radius.
#
# Overall Plan:
# 1. Write the function to take the arguments as the radius of the sphere.
# 2. Use the formula for the area and the volume.   
# 3. Define a main function to call the functions and test the methods.
#
# import the necessary python libraries
import math

#Define sphereArea function:
def sphereArea(radius):
    area = 4 * math.pi * (radius * radius)
    return(area)
#Define sphereVolume function:
def sphereVolume(radius):
    volume = (4 / 3) * (math.pi * (radius * radius))
    return(volume)
#Define main function for testing.
def main():
    radius = float(input("Enter the radius of the sphere: "))

    area = sphereArea(radius)
    volume = sphereVolume(radius)

    print("The area is: ", area)
    print("The volume is: ", volume)

main()

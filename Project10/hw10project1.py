#! /usr/bin/python
# Exercise No.   01
# File Name:     hw10project1.py
# Programmer:    John Rollinson
# Date:          11/02/2019
#
# Problem Statement:
# Write a class to represent the geometric solid sphere. Your class should implement the following
# methods:
#   Creates a sphere having the given radius.
#   Returns the radius of this sphere.
#   Returns the surface area of this sphere.
#   Returns the volume of this sphere.
# Then test the class in the main method.
#
# Overall Plan:
# 1. Define a class Spheres which contains its features for calculating the surface area and volume.    
# 2. Define a constructor of a class _init_() which will set the radius of a sphere.
# 3. Define a method getRadius() which will obtain an input for the radius from the user. 
# 4. surfaceArea() which will calculate a surface area of a sphere and a method volume() which will
#       calculate a volume of a sphere.
# 5. Define a method main() which will print the results.
#
# import the necessary python libraries
import math

class Spheres:
    def __init__(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def surfaceArea(self):
        return 4 * math.pi * (self.radius ** 2)
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

def main():
    print("Program to calculate the surface area and volume of a sphere.\n")

    # ra = radius; sp = sphere
    ra = eval(input("Enter radius of the sphere: "))
    sp = Spheres(ra)

    print("The volume of the sphere is:", round(sp.volume(), 2))
    print("The surface area of the sphere is:", round(sp.surfaceArea(), 2))

main()

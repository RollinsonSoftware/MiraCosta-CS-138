#! /usr/bin/python
#Exercise No.  01
#File Name:    hw4project1.py
#Programmer:   John Rollinson
#Date: 9/14/2019
#
#Problem Statement: (what you want the code to do)
#Program to calculate and print the length and slope of the line.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Record the two mouse clicks from the user.  
#2. Create two points from those x and y coordinates of both clicks.
#3. Draw the line segment to the GUI. 
#4. Find the midpoint and of the line segment and color that pixel cyan.
#5. Find the slope and length of the line using the given formulas.
#6. Display the calculated length and slope on the GUI.
#
#import necessary python libraries
#Create main function
import math
from graphics import*

def main():
    win = GraphWin("Line Segement", 500, 500)

    #Console outuput aswell:
    print("Outputing instructions to GUI.")
    click = Text(Point(200,10), "Click on two loactions in the graphics window.")
    click.draw(win)

    print("Taking mouse positions from the user.")
    p1 = win.getMouse()
    p2 = win.getMouse()

    print("Forming line segment.")
    lineSeg = Line(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))

    print("Finding midpoint.")
    midpoint = lineSeg.getCenter()
    midpoint.setFill('cyan')
    midpoint.draw(win)

    lineSeg.draw(win)

    print("Calculating the difference difference of X axes and Y axes respectively.")
    diffX = p2.getX() - p1.getX()
    diffY = p2.getY() - p1.getY()

    print("Calculating the slope and length of the line segement.")
    slope = diffY / diffX
    #Distance formula:
    length = math.sqrt(abs((diffX**2) - (diffY**2)))

    #Output:
    lengthOut = Text(Point(220, 50), "The length of the line is: " + str(length))
    lengthOut.draw(win)

    slopeOut = Text(Point(220, 80), "The slope of the line is: " + str(slope))
    slopeOut.draw(win)

    ex = Text(Point(100, 400), "Click to exit.")
    ex.setSize(12)
    ex.draw(win)

    #getMouse() function is used to hold the graphics.
    win.getMouse()
    #Finally close() method is used to close the GUI screen on mouse click.
    win.close()
    print("Exiting program...")
    
main()

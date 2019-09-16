#! /usr/bin/python
#Exercise No.  03
#File Name:    hw4project3.py
#Programmer:   John Rollinson
#Date: 9/14/2019
#
#Problem Statement: (what you want the code to do)
#To draw the house on five mouse clicks.
#
#Overall Plan (step-by-step,how you want the code to make it happen):
#1. Print message to the GUI that specifies the purpose of each mouse click.
#2. Two coordinates of mouse locations are taken from the user.
#3. Create a rectangle by joining the given points.
#4. Get the next click from the user.
#5. Calculate the door width as the 1/5th of the width of the house frame. 
#6. Calculate the upper-left and lower-right corners of the door.
#7. Get the fourth mouse click from the user.
#8. Calculate the side of the square window as half of the width of the door.
#9. Calculate the upper-left and lower-right corners of the window.
#10. Draw the window and get the final mouse click from the user.
#11. Draw the lines for joining the roof with the top of the house.
#
#import necessary python libraries
#Create main function
import math
from graphics import*

def main():
    win = GraphWin("House", 500, 500)

    click = Text(Point(200, 50), "Click on two locations to make a rectangular house. \n-Third for the center of the door. \n-Fourth for the center of the square window. \n-The last for the top of the roof.")
    click.draw(win)

    #Building:
    p1 = win.getMouse()
    p2 = win.getMouse()
    rec = Rectangle(p1, p2)
    rec.draw(win)

    #Door:
    p3 = win.getMouse()
    doorWidth = (p2.getX() - p1.getX()) / 5
    upperLeft = Point((p3.getX() - (doorWidth / 2)), p3.getY())
    lowerRight = Point((p3.getX() + (doorWidth / 2)), p2.getY())
    door = Rectangle(upperLeft, lowerRight)
    door.draw(win)

    #Window:
    p4 = win.getMouse()
    side = (lowerRight.getY() - upperLeft.getY()) / 2
    s1 = Point((p4.getX() - (side / 2)), (p4.getY() - (side / 2)))
    s2 = Point((p4.getX() + (side / 2)), (p4.getY() + (side / 2)))
    window = Rectangle(s1, s2)
    window.draw(win)

    #Roof:
    p5 = win.getMouse()
    length1 = Line(p5, p1)
    length2 = Line(p5, Point(p2.getX(), p1.getY()))
    length1.draw(win)
    length2.draw(win)

    #Exit program:
    ex = Text(Point(100, 400), "Click to exit.")
    ex.setSize(12)
    ex.draw(win)
    win.getMouse()
    win.close()
    
main()

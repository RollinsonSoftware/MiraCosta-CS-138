#! /usr/bin/python
# Exercise No.   Extra Credit
# File Name:     hw6extraCredit.py
# Programmer:    John Rollinson
# Date:          9/29/2019
#
# Problem Statement:
# Use the described function to write a program that draws a circle and then
#       allows the user to click the window 10 times. Each time the user clicks
#       the circle is moved where the user clicked.
#
# Overall Plan:
# 1. define a method to find the distance between 2 points and then move the circle
# 2. define a method to indicate the point where the mouse will be clicked.
# 3. define a method to draw the bottom menu to display text.
# 4. define a method to display the text to the user.
# 5. define a method to locate the ball first at center(0, 0)
# 6. define a main method to display the GUI.
#
# import the necessary python libraries
from graphics import*

def move_to(shape, new_center):
    old_center = shape.getCenter()
    x = new_center.getX() - old_center.getX()
    y = new_center.getY() - old_center.getY()
    shape.move(x, y)

def indicate(win):
    for i in range(-10, 11):
        white_L = color_rgb(201, 201, 201)
        h_arm = Line(Point(i, -10), Point(i, 10))
        h_arm.setFill(white_L)
        h_arm.draw(win)
        v_arm = Line(Point(-10, i), Point(10, i))
        v_arm.setFill(white_L)
        v_arm.draw(win)

def menu_bar(win):
    light_grey = color_rgb(98, 98, 98)
    menu_bg = Rectangle(Point(-10, -8), Point(10, -10))
    menu_bg.setOutline(light_grey)
    menu_bg.setFill(light_grey)
    menu_bg.draw(win)
    light_green = color_rgb(180, 180, 40)
    menu_decor = Oval(Point(-11, -9.5), Point(11, -11))
    menu_decor.setOutline(light_green)
    menu_decor.setFill(light_green)
    menu_decor.draw(win)

def intro_text(win):
    words = Text(Point(0, -8.75), "Click anywhere to move the circle.")
    words.setFace('times roman')
    words.setFill('grey')
    words.draw(win)
    return words

def first_ball(win):
    balls = Circle(Point(0, 0), 2)
    balls.setFill('green')
    balls.setOutline('black')
    balls.draw(win)
    return balls

def main():
    win = GraphWin('10 times moving circle', 500, 500)
    win.setCoords(-10, -10, 10, 10)
    indicate(win)
    menu_bar(win)
    words = intro_text(win)
    balls = first_ball(win)

    for i in range(10):
        new_center = win.getMouse()
        move_to(balls, new_center)
    
    words.setText('Bye! Click to close.')
    win.getMouse()
main()
    

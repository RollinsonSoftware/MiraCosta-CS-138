#! /usr/bin/python
# Exercise No.   2
# File Name:     hw4project2.py
# Programmer:    John Rollinson
# Date:          9/14/2019
#
# Problem Statement: Ask the user to enter three numbers, calculate the sum of 
# These three numbers and the product, and display the sum and product to the screen.
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for three integers
# 3. Calculate the sum of the integers
# 4. Calculate the product of the integers
# 5. Print the sum of the integers to the screen
# 6. Print the product of the integers to the screen
#
# import the necessary python libraries
# for this example none are needed
from graphics import*

def main():
    
    # Print a message to the screen
    print("Hello!")
    print("I can add and multiply three numbers for you.")

    win = GraphWin("My First Program.", 400, 500)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    #Draw the interface
    Text(Point(1, 3), "Enter a few whole numbers:").draw(win)
    Text(Point(1, 1), "Sum of the numbers:").draw(win)
    Text(Point(1, 0.75), "Product of the numbers:").draw(win)
    
    input = Entry(Point(2, 3), 5)
    input.setText("0.0")
    input.draw(win)

    outputSum = Text(Point(2, 1), "")
    outputSum.draw(win)
    outputProduct = Text(Point(2, 0.75), "")
    outputProduct.draw(win)

    #Button
    button = Text(Point(1.5, 2.0), "Enter")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    #User Input.
    win.getMouse()
    num1 = eval(input.getText())
    print("User entered: ", num1)
    input.setText("0.0")
    
    win.getMouse()
    num2 = eval(input.getText())
    print("User entered: ", num2)
    input.setText("0.0")

    button.setText("Calculate")
    win.getMouse()
    num3 = eval(input.getText())
    print("User entered: ", num3)
    input.setText("0.0")

    #Calculations
    sum = num1 + num2 + num3
    product = num1 * num2 * num3

    #Output
    outputSum.setText(sum)
    outputProduct.setText(product)
    
    button.setText("Quit")
    win.getMouse()
    win.close()

main()

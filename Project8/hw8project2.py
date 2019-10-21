#! /usr/bin/python
# Exercise No.   02
# File Name:     hw8project2.py
# Programmer:    John Rollinson
# Date:          10/20/2019
#
# Problem Statement:
# Write a program that converts a color image to grayscale. The user supplies
# the name of a file containing a GIF or PPM image, and the program loads the
# image and displays the file. At the click of the mouse, the program converts
# the image to grayscale. The user is then prompted for a filename to store the
# grayscale image in.
#
# Overall Plan:
# 1. Import the graphics library for using graphics functions
# 2. Define the main function
# 3. Get the input and output file names
# 4. Draw the image at a particular position
# 5. Get the image width and height to iterate
# 6. Change to greyscale based on the logic provided when user clicks on the image.
#
# import the necessary python libraries
from graphics import*

def main():
    #Get input file name
    input_filename = input("Enter the name of the file: ")
    #Get the output file name
    output_filename = input("What will be the name of the new file?: ")

    #Set the image position
    my_image = Image(Point(120, 120), input_filename)
    #Get the width and height of the image
    image_width = my_image.getWidth()
    image_height = my_image.getHeight()

    #Set graphics window
    win = GraphWin("rgb", image_width, image_height)
    my_image.draw(win)

    row = 0
    column = 0
    win.getMouse()

    #Iterate through the image pixels using loops
    for row in range(image_width):
        for column in range(image_height):
            #Set to greyscale
            r, g, b = my_image.getPixel(row, column)
            brightness = int(round(0.299 * r + 0.587 * g + 0.144 * b))
            #Set the new pixel
            my_image.setPixel(row, column, color_rgb(brightness, brightness, brightness))
            #Update the window
            win.update()
    
    #Save the file to the new location
    my_image.save(output_filename)
    win.getMouse()
    win.close()
    
main()

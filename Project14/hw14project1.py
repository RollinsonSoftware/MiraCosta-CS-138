#! /usr/bin/python
# Exercise No.   01
# File Name:     hw14project1.py
# Programmer:    John Rollinson
# Date:          12/04/2019
#
# Problem Statement:
# Write a program to compare sorting results. Compare the sort times of
# python standard sort (tim sort), selection sort, and merge sort. For the
# list sizes fill random lists of size 5000, 50,000, and 5,000,000.
#
# Overall Plan:
# 1. define a merge helper method to split the list in half.
# 2. define a recursive mergeSort method to sort and merge each half.
# 3. define a selectionSort method that implements the selection sort algorithm.
# 4. define a print array helper method that will print a list of any size. 
# 5. define a main method that outputs the sorted and unsorted lists, testing
#       each sorting algorithm: python built in sort(), selection sort, and merge sort.
# 6. Write the small, medium, and big lists to a text file. 
#
# import the necessary python libraries
import sys
import random
import datetime

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def mergeSort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = mergeSort(nums[:mid])
    right_list = mergeSort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)

def selectionSort(arr):
    # Traverse through all array elements 
    for i in range(len(arr)): 
          
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def printArray(arr):
    #prints an entire array
    for i in range(len(arr)): 
        print("%d" %arr[i]),

#Driver function for testing and output.        
def main():
    print("This can be demonstrated better with a smaller list")
    print("so I will use the test lists for the screen shots.")

    test1 = random.sample(range(0, 101), 6)
    test2 = random.sample(range(0, 101), 6)
    test3 = random.sample(range(0, 101), 6)

    #Testing Merge Sort:
    print("TESTING MERGE SORT...")
    print ("Original array:")
    printArray(test1)
    print ("Sorted array:")
    test1 = mergeSort(test1)
    printArray(test1)

    #Testing Selection Sort:
    print("TESTING SELECTION SORT...")
    print ("Original array:")
    printArray(test2)
    print ("Sorted array:")
    selectionSort(test2)
    printArray(test2)

    #Testing built-in python sort() function:
    print("TESTING THE BUILT IN SORT() FUNCTION FROM PYTHON...")
    print ("Original array:")
    printArray(test3)
    print ("Sorted array:")
    test3.sort()
    printArray(test3)

    #Now that we know it works, I will make this massive text document
    #   per the homework instructions...
    print("Constructing lists...")
    small = random.sample(range(0, 5000), 5000)
    medium = random.sample(range(0, 50000), 50000)
    large = random.sample(range(0, 5000000), 5000000)

    print("Sorting lists...")
    small = mergeSort(small)
    selectionSort(medium)
    large.sort()

    print("Writing lists to hw14project1.txt...")
    with open('hw14project1.txt', 'w') as file:
        file.write("Small list sorted:")
        for num in small:
            file.write("%i\n" % num)
        file.write("Medium list sorted:")
        for num in medium:
            file.write("%i\n" % num)
        file.write("Large list sorted:")
        for num in large:
            file.write("%i\n" % num)
    
main()

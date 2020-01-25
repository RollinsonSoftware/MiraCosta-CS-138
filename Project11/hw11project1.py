#! /usr/bin/python
# Exercise No.   01
# File Name:     hw11project1.py
# Programmer:    John Rollinson
# Date:          11/10/2019
#
# Problem Statement:
# Write an algorithm for each of the following Python operations and test your algorithm
# by writing it up in a suitable function. For example, as a function, reverse(myList) should do
# the same as myList.reverse(). Obviously, you are not allowed to use the corresponding Python method
# to implement your function. 
#
# Overall Plan:
# 1. Take a list of numbers and store it into variable list3. 
# 2. Take the number and store it into variable x.
# 3. Create user define functions count(), isin(), index() with list and number as arugments that
#       works similar to build in functions. 
# 4. Create user define functions reverse() and sort() with list as argument that works similar to
#       built in functions.
# 5. Call and Print results of user define functions.
#
# import the necessary python libraries
def count(list1, x):
    count = 0
    for i in list1:
        if i == x:
            count = count + 1
    return count
def isin(list1, x):
    n = len(list1)
    while(n - 1 > 0):
        if(list1[n - 1] == x):
            return 1
            break
        else:
            n = n - 1
            return 0
def index(list1, x):
    n = len(list1)
    for i in range(n):
        if(list1[i] == x):
            return(i)
        else:
            i = i + 1
            return -1
def reverse(list1):
    rlist = []
    n = len(list1)
    for i in range(n):
        rlist.append(list1[n - 1])
        n = n - 1
    return rlist
def sort(list1):
    slist = []
    n = len(list1)
    for i in range(n):
        for i1 in range(n - 1):
            if(list1[i1] >= list1[i1 + 1]):
                x = list1[i1]
                list1[i1] = list1[i1 + 1]
                list1[i1 + 1] = x
    return list1
def main():
    list3 = [2, 0, 1, 2, 5, 8, 2]
    x = 2
    print("Value for X:", x)
    print("Elements in List:", list3)
    cnt = count(list3, x)
    if cnt == 0:
        print("List {0} does not contains{1}".format(list3, x))
    else:
        print("count( {0},  {1}) = {2}".format(list3, x, cnt))
        i1 = isin(list3, x)
    if i1 == 0:
        print("List {0} does not contains{1}".format(list3, x))
    else:
        print("isin({0} , {1}) = {2}".format(list3, x, "true"))
        ind = index(list3, x)
    if ind == -1:
        print("List {0} does not contains{1}".format(list3, x))
    else:
        print("index({0}, {1}) = {2}".format(list3, x, ind))
        print("Original List:", list3)
        rlist = reverse(list3)
        print("Reverse List: {0}".format(rlist))
        sort(list3)
        print("Sorted list: {0}".format(list3))
main()
        








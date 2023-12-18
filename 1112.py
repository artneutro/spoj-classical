#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 18/12/2023
# Updates:
# 
# SPOJ
# Problem 1112
# NSTEPS - Number Steps
# https://www.spoj.com/problems/NSTEPS/
#

#
# Print the value in the coordinates (x,y) provided
#

cases = int(input())
if cases == 0 :
    exit() ;
while (cases > 0) :
    # Read the values of (x, y)
    x_str, y_str = (input()).split()
    x, y = int(x_str), int(y_str)
    # Case when x == y (main line)
    if (x == y) :
        if x%2 == 0 :
            print(x*2)
        else :
            print(x*2 - 1)
    # Case when x == y + 2 (below line)
    elif (x == y + 2) :
        if x%2 == 0 :
            print(x+y)
        else :
            print(x+y - 1)
    # Case when x == y
    else :
        print("No Number")
    # Decrease the case counter
    cases = cases - 1








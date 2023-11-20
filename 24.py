#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 15/11/2023
# Updates:
#
# SPOJ
# Problem 24
# FCTRL2 - Small factorials
# https://www.spoj.com/problems/FCTRL2/
#

# Divide-and-conquer factorial algorithm
# is already implemented in the Python libraries!
# Based in the formula from http://www.luschny.de/math/factorial/binarysplitfact.html
import math

# Get the number of cases
cases = int(input())
counter = 1
# Main program
if cases <= 0 :
    exit
while counter <= cases :
    n = int(input())
    print(math.factorial(n))
    counter = counter+1
    










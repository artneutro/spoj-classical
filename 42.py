#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 01/11/2023
# Updates:
# 
# SPOJ
# Problem 42
# ADDREV - Adding Reversed Numbers
# https://www.spoj.com/problems/ADDREV/
#

# Get the number of cases
cases = int(input())
counter = 0
# Main program
if cases <= 0 :
    exit
while counter < cases :
    low_s, high_s = input().split(" ")
    low = int(low_s[::-1])
    high = int(high_s[::-1])
    sum = low+high
    print(int(str(sum)[::-1]))
    print()
    counter = counter+1


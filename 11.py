#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 15/11/2023
# Updates:
#
# SPOJ
# Problem 11
# FCTRL - Factorial
# https://www.spoj.com/problems/FCTRL/
#

# Get the number of cases
cases = int(input())
counter = 1
# Main program
if cases <= 0 :
    exit
while counter <= cases :
    check = int(input())
    init = 5
    zeroes = 0
    # Z(N) = S(i=1,k)[n/5**i]
    while check/init >= 1 :
        zeroes = zeroes + int(check / init)
        init = init*5
    print(zeroes)
    counter = counter+1
    









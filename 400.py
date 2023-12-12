#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 12/12/2023
# Updates:
# 
# SPOJ
# Problem 400
# TOANDFRO - To and Fro
# https://www.spoj.com/problems/TOANDFRO/
#

#
# Print the unencrypted message from Mo & Larry encryption method
#

while True :
    value = int(input())
    if value == 0 :
        break ;
    else :
        text = input()
        # Split the message in items of size n
        list_fragments = [text[i:i+value] for i in range(0, len(text), value)]
        check = 0
        # Reverse the odd lines
        for fragment in list_fragments :
            if check%2 == 0 :
                pass
            else :
                list_fragments[check] = fragment[::-1]
            check = check + 1
        # Print the encrypted message
        pointer = 0
        while pointer < value :
            for fragment in list_fragments :
                print(fragment[pointer], end = "")
            pointer = pointer + 1
        print()









#!/usr/bin/python3
#
# Author: Jose Lo Huang
# Creation Date: 20/11/2023
# Updates:
#
# SPOJ
# Problem 4
# ONP - Transform the Expression
# https://www.spoj.com/problems/ONP/
#

# Convert expression from algebraic to Reverse Polish Notation (RPN)
def rpn(exp) :
    valid_op = ['+', '-', '*', '/', '^']
    operators = []
    solution = ''
    for i in exp:
        if i == '(' :
        # If open parenthesis, do nothing
            continue
        elif i in valid_op :
        # If it is an operator, store it in the op stack
            operators.append(i)
        elif i == ')' :
        # Each time it finds a closing parenthesis
        # it takes one operator from the op stack
            solution = solution + operators.pop()
        else :
        # Anything else (variables), add it to the solution
            solution = solution + i
    return solution
            

# Get the number of cases
cases = int(input())
counter = 1
# Main program
if cases <= 0 :
    exit
while counter <= cases :
    exp = input()
    print(rpn(exp))
    counter = counter+1
    



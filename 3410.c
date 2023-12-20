/**
#
# Author: Jose Lo Huang
# Creation Date: 20/12/2023
# Updates:
#
# SPOJ
# Problem 3410
# SAMER08F - Feynman
# https://www.spoj.com/problems/SAMER08F/
#

#
# Print the number of squares in a NxN grid using the value of N
#
**/

#include <stdio.h>

int main(void)
{
    while (0==0) {
        // Get the next case
        int next_case ;
        scanf("%d", &next_case) ;
        if (next_case == 0) {
            return 0 ;
        }
        // The number of squares in a NxN grid is S(n*n) for n=0..N
        int solution = 0 ;
        while (next_case > 0) {
            solution = solution + (next_case * next_case) ;
            next_case = next_case - 1 ;
        }
        printf("%d\n", solution) ;
    }
  return 0;
}










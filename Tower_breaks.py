#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n = number of towers
#  2. INTEGER m = height of tower
#
number_of_moves_left = 0

def towerBreakers(n, m):
    
    for i in range(1, m-1):
        if m % i == 0:
            factor = i
            number_of_moves_left = +1
            result = towerBreakers(factor)
            print(number_of_moves_left)
            print(result)
        if number_of_moves_left*n % 2 != 0:
            winner = 1
            break
        else:
            winner = 2
        return(winner)
    
                    

if __name__ == '__main__':
   
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(result)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

# Sample Input:
# 2 3
# 2 4
# 16 32 96
# Sample Output:
# 3
#

def getTotalX(a, b):


    inBetweens = []
    for i in range(a[len(a)-1], b[0]+1):
        inBetweens.append(i)
    print(inBetweens)

    factors_of_a = []
    factors_of_b = []
    
    for i in inBetweens:
        is_factor = True
        for j in a:
            if i % j != 0:
                is_factor = False
        if is_factor:
            factors_of_a.append(i)
    print(factors_of_a)

    for i in factors_of_a:
        is_factor = True
        for j in b:
            if j % i != 0:
                is_factor = False
        if is_factor:
            factors_of_b.append(i)
    print(factors_of_b)


    getTotalX = len(factors_of_b)

    
    return (getTotalX)
        


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
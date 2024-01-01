#!/bin/python3


import math
import os
import random
import re
import sys


# Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.
# 
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar


# Sample Input: 
#   6 3
#   1 3 2 6 1 2 
# Sample Output
#   5


def divisibleSumPairs(n, k, ar):
    result = 0
    for index_i, i in enumerate(ar):
        for index_j, j in enumerate(ar[index_i+1:n]):
            if (i + j) % k == 0:
                result += 1
                print(index_i, index_j)
    return (result)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)

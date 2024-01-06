#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
arr = [5, 6, 8, 11]


def balancedSums(arr):
    array_total = 0
    sumsBalanced = False
    for i in arr:
        array_total = array_total + i

    left_sum = 0
    right_sum = array_total - arr[0]

    for index_j, j in enumerate(arr):
        if index_j != 0:
            left_sum = left_sum+arr[index_j-1]
            right_sum = right_sum-j
        if right_sum == left_sum:
            sumsBalanced = True
            break    

    if sumsBalanced:
        return ("YES")
    else:
        return ("NO")
    

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result + '\n')


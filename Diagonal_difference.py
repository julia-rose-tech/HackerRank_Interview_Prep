#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Sample Input:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample output: 
# 15


def diagonalDifference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    
    for i in range(len(arr)):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][len(arr) - 1 - i]
    
    answer = abs(left_to_right_diagonal-right_to_left_diagonal)
    return (answer)
     


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)



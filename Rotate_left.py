#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
d = 3
arr = [1, 2, 3, 4]

def rotateLeft(d, arr):
    
    last_index = len(arr)-1
    for i in range(d):
        temp_arr = [0]*len(arr)
        for index_j, j in enumerate(arr):
            if index_j == 0:
                temp_arr[last_index] = j
            else:           
                temp_arr[index_j-1] = j
        arr = temp_arr
    return(temp_arr)
        


# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# d = int(first_multiple_input[1])

# arr = list(map(int, input().rstrip().split()))

result = rotateLeft(d, arr)

print(result)
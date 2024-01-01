#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
# k = 4
# arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

# k = 2
# arr = [1, 2, 1, 2, 1]

k = 5
arr = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
# Output = 1335

def maxMin(k, arr):
    sorted_array = sorted(arr)
    fair_n = sorted_array[len(sorted_array)-1]
    for index_j, j in enumerate(arr[:len(arr)-k+1]):
        new_array = sorted_array[index_j:index_j+k]   
        if new_array[k-1] - new_array[0] < fair_n:
            fair_n = new_array[k-1] - new_array[0]
    return(fair_n)

 

# n = int(input().strip())

# k = int(input().strip())

# arr = []

# for _ in range(n):
#     arr_item = int(input().strip())
#     arr.append(arr_item)

result = maxMin(k, arr)
print(result)


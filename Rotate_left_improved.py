#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'rotateLeft' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d: The number of rotations to perform.
#  2. INTEGER_ARRAY arr: The array to rotate.

def rotateLeft(d, arr):
    # Create a new array of the same length as 'arr'.
    rotated_arr = [0] * len(arr)
    last_index = len(arr) - 1
    
    # Loop through the elements of 'arr'.
    for index_j, j in enumerate(arr):
        if index_j <= d - 1:
            # If the current index is within the first 'd' elements, place 'j' at the end of the new array.
            rotated_arr[last_index + index_j - d + 1] = j
        else:
            # Otherwise, place 'j' at the adjusted index.
            rotated_arr[index_j - d] = j
            
    return rotated_arr

# Read the input values.
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))

# Call the 'rotateLeft' function and print the result.
result = rotateLeft(d, arr)
print(result)

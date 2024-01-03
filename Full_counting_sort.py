#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

# Sample Input:
# 20
# 0 ab
# 6 cd
# 0 ef
# 6 gh
# 4 ij
# 0 ab
# 6 cd
# 0 ef
# 6 gh
# 0 ij
# 4 that
# 3 be
# 0 to
# 1 be
# 5 question
# 1 or
# 2 not
# 4 is
# 2 to
# 4 the
# Sample Output: - - - - - to be or not to be - that is the question - - - -

def countSort(arr):
    """
    Counting Sort implementation for a list of string integer pairs.
    
    Args:
        arr (list): A list of string integer pairs, where the first element
                    is the integer to determine the sorting order, and the
                    second element is the string to be sorted.
                    
    Returns:
        None: The function prints the sorted elements separated by spaces.
    """
    for i in range(len(arr) + 1):
        if i == 0:
            sorted_arr = [[] for _ in range(len(arr) // 2 + 1)]
        elif i <= len(arr) // 2:
            index = int(arr[i - 1][0])
            sorted_arr[index].append(chr(45))
        else:
            index = int(arr[i - 1][0])
            sorted_arr[index].append(arr[i - 1][1])
    print(" ".join([element for row in sorted_arr for element in row]))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

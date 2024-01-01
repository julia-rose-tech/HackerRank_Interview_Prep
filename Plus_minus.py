#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# The function accepts INTEGER_ARRAY arr as parameter.


# Sample Input:
#   5
#   1 1 0 -1 -1

# Sample Output
#   0.40000
#   0.40000
#   0.20000

def plusMinus(arr):
    count_negatives = sum(1 for num in arr if num < 0)
    count_positives = sum(1 for num in arr if num >0)
    count_zeros = sum(1 for num in arr if num ==0)
    
    positive_ratio=count_positives/len(arr)
    negative_ratio=count_negatives/len(arr)
    zeros_ratio=count_zeros/len(arr)
    
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zeros_ratio:.6f}")


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
print(plusMinus)
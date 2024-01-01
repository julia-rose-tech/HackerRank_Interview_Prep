#!/bin/python3

import math
import os
import random
import re
import sys

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# The function accepts INTEGER_ARRAY arr as parameter.
#

# Sample Input
#   1 3 5 7 9

# Sample Output
#   16 24

def miniMaxSum(arr):
    lowest_number = min(arr)
    highest_number = max(arr)
    
    max_sum = sum(arr)-lowest_number
    min_sum = sum(arr)-highest_number
    
    print(min_sum, max_sum)

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)

print(miniMaxSum)

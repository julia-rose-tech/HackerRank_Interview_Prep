#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

# Sample Input 1

# 12
# -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 
# Sample Output 1

# -520 -470 -20 30

def closestNumbers(arr):
    sorted_Arr = sorted(arr)
    min_difference = sorted_Arr[n-1]-sorted_Arr[0]
    returned_array = []
    for i in range(0, n-1):
        if sorted_Arr[i+1]-sorted_Arr[i]<min_difference:
            min_difference = sorted_Arr[i+1]-sorted_Arr[i]
    for i in range(0, n-1):
        if sorted_Arr[i+1]-sorted_Arr[i] == min_difference:
            returned_array.append(sorted_Arr[i])
            returned_array.append(sorted_Arr[i+1])
    return (returned_array)



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)
    
    print(result)

# ChatGPT solution:
# def closestNumbers(arr):
#     arr.sort()  # Sort the input array in ascending order
#     n = len(arr)
    
#     min_difference = float('inf')
#     returned_array = []

#     for i in range(1, n):
#         diff = arr[i] - arr[i - 1]

#         if diff < min_difference:
#             min_difference = diff
#             returned_array = [arr[i - 1], arr[i]]
#         elif diff == min_difference:
#             returned_array.extend([arr[i - 1], arr[i]])

#     return returned_array

# if __name__ == '__main__':
#     n = int(input().strip())
#     arr = list(map(int, input().rstrip().split()))

#     result = closestNumbers(arr)
    
#     print(*result) 
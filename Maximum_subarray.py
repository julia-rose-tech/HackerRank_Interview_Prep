#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Example Input:
# 1
# 5
# -2 -3 -1 -4 -6
# Expected Output:
# -1 -1

# Attempt 2 Using Kadanes Algo


def maxSubarray(arr):
    """
    Finds the maximum subarray sum within the given array using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers representing the input array.
        
    Returns:
        tuple: A tuple containing two integers:
            - The maximum subarray sum (`max_so_far`).
            - The maximum sum of positive elements in the array (`seq_max`).
    
    Note:
        This function calculates the maximum subarray sum using Kadane's Algorithm, which
        efficiently handles both positive and negative numbers. If all elements in the array 
        are negative, the maximum subarray sum will be the maximum element in the array.
    """
    len_arr = len(arr)
    max_so_far = float('-inf')
    max_ending_here = 0
    seq_max = 0

    for i in range(0, len_arr):
        # Calculate seq_max
        if arr[i] > 0:
            seq_max += arr[i]
        # Kadane's Algo
        max_ending_here = max_ending_here + arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    # Check if seq_max is zero, then the arr may have all been neg numbers. Hence, the seq max should be the man of these values rather than the sum calculated about. 
    if seq_max == 0:
        seq_max = max(arr)
     
    return max_so_far, seq_max





# First Attempt. This code works for the smaller cases, not the larger 
# def maxSubarray(arr):
#     max_seq_sum = 0
#     max_sub_arr_sum = 0
#     all_negatives = True
#     for i in arr:
#         if i > 0:
#             max_seq_sum += i
#             all_negatives = False
#     if all_negatives == True:
#         max_seq_sum = max(arr)
#         max_sub_arr_sum = max(arr)
#         return max_sub_arr_sum, max_seq_sum

#     right_array_sum = 0
#     left_array_sum = 0
#     start_sub_array_index = 0
#     end_sub_array_index = len(arr)-1
#     for i in range(len(arr)-1):
#         right_array_sum += arr[i]
#         left_array_sum += arr[len(arr)-1-i]
#         if right_array_sum < 0:
#             start_sub_array_index = i+1
#             right_array_sum = 0
#             print("New starting index is:"+str(start_sub_array_index))
#         if left_array_sum < 0:
#             end_sub_array_index = len(arr)-2-i
#             left_array_sum = 0
#             print("New ending index is:"+str(end_sub_array_index))
    
#     sub_array = arr[start_sub_array_index:end_sub_array_index+1]
#     print(arr[start_sub_array_index:end_sub_array_index+1])
#     for i in sub_array:
#         max_sub_arr_sum += i
#     return max_sub_arr_sum, max_seq_sum

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        print(result)
      

  

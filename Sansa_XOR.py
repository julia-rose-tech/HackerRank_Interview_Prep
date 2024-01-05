#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def sansaXor(arr):
    """
    Calculate the XOR of non-repeating subarrays of the input array.

    Parameters:
    arr (list): The input list of integers.

    Returns:
    int: The XOR result of all non-repeating subarrays.

    This function computes the XOR of all non-repeating subarrays of the given input array.
    It iterates through the elements of the array, calculates the XOR of each element with
    a specific formula, and accumulates the XOR results. The final XOR result is returned.
    """
    N = len(arr)  # Get the length of the input array
    ans = 0       # Initialize the result variable to store the XOR result

    # Iterate through the elements of the input array
    for i in range(N):
        # Check if the number of subarrays an element belongs to is odd or even
        # based on a mathematical formula. If it's odd, XOR it with the result.
        if (N*(i+1) - i*(i+1)) % 2 != 0:
            ans = ans ^ arr[i]  # XOR the current element with the result

    return ans  # Return the final XOR result


# Each value appears N(i+1) - i(i+1) times. Reminder x ^ x = 0
# For example, arr = [1, 2, 3] ==> 1^ 2^ 3^(1^2)^(2^3)^(1^2^3)
# 1 & 3 occurs 3 times, and 2 occurs 4 times. Therefore all the 2's cancel out, and all but one 1 and one 3 cancel out. 
# The formula N(i+1) - i(i+1) works as follows:
# N = 3, i = 0 ==> 3(1)-0(1) = 3
# N = 3, i = 1 ==> 3(2)-1(2) = 4
# N = 3, i = 2 ==> 3(3)-2(3) = 3



if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        print(str(result) + '\n')



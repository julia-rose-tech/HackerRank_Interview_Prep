#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts the following parameters:
#  1. INTEGER_ARRAY arr: The original array containing numbers.
#  2. INTEGER_ARRAY brr: The modified array containing numbers with some missing.

def missingNumbers(arr, brr):
    """
    Find and return missing numbers from the modified array brr with respect to the original array arr.

    Args:
    arr (list of integers): The original array containing numbers.
    brr (list of integers): The modified array containing numbers with some missing.

    Returns:
    list of integers: A list of missing numbers.

    Example:
    If arr = [1, 2, 3, 4] and brr = [1, 2, 3, 5], the missingNumbers function will return [5],
    as 5 is missing from the modified array brr compared to the original array arr.
    """
    unique_brr = set(brr)
    missing_numbers = []
    for i in unique_brr:
        count_i_arr = arr.count(i)
        count_i_brr = brr.count(i)
        if count_i_brr > count_i_arr:
            missing_numbers.append(i)
    return missing_numbers

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))

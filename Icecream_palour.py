#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m: The amount of money they have to spend on ice cream.
#  2. INTEGER_ARRAY arr: An array of integers representing the cost of different flavors of ice cream.

# Example usage:
# m = 4
# arr = [1, 4, 5, 3, 2]
# The function should return [1, 4], indicating the indices of the flavors that sum up to the available money.

def icecreamParlor(m, arr):
    # Nested loop to iterate through all pairs of flavors
    for index_i, i in enumerate(arr):
        for index_j, j in enumerate(arr):
            # Ensure that we don't compare the same flavor with itself
            if index_i < index_j:
                # Check if the current pair of flavors sum up to the available money
                if m - i == j:
                    # Return the indices of the selected flavors (+1 to make them 1-based indices)
                    return [index_i+1, index_j+1]

# Example usage:
m = 4
cost = [1, 4, 5, 3, 2]
result = icecreamParlor(m, cost)
print(result)  # Output should be [1, 4], as it indicates the flavors that can be purchased with the available money.

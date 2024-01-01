#!/bin/python3

import math
import os
import random
import re
import sys

# Sample Input:
# 5
# 1 1 1 3 3


# Sample Output:
# 1 3 3

# Sample Input 2:
# 6
# 1 1 1 2 3 5
# Output: 
# 1 1 1
#

# Sample Output 3:
# 3
# 1 2 3

# Sample Output:
# -1
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
# Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. Return an array of the lengths of its sides as  integers in non-decreasing order.

# If there are several valid triangles having the maximum perimeter:

# Choose the one with the longest maximum side.
# If more than one has that maximum, choose from them the one with the longest minimum side.
# If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return -1.


def maximumPerimeterTriangle(sticks):
    sorted_array = sorted(sticks, reverse=True)
    for i in range(len(sorted_array) - 2):
        if sorted_array[i+1]+sorted_array[i+2] > sorted_array[i]:
            answer = (sorted_array[i+2], sorted_array[i+1], sorted_array[i])
            break
        else:
            answer = [-1]
    return(answer)


if __name__ == '__main__':
    
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(result)
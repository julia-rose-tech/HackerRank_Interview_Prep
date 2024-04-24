#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def stack_sums(h):
    """
    Calculates the cumulative sums of a given stack represented by a list.

    Parameters:
        h (list): A list representing the heights of the stack.

    Returns:
        list: A list containing the cumulative sums of the stack from bottom to top.

    Example:
        >>> stack_sums([3, 2, 1])
        [0, 3, 5, 6]
    """
    sums_h = [0]
    cumulative_sum = 0
    for i in reversed(h):
        cumulative_sum += i
        sums_h.append(cumulative_sum)
    return sums_h

def equalStacks(h1, h2, h3):
    """
    Finds the highest common sum achievable by removing elements from the top of three stacks
    to make them equal in height.

    Parameters:
        h1 (list): A list representing the heights of the first stack.
        h2 (list): A list representing the heights of the second stack.
        h3 (list): A list representing the heights of the third stack.

    Returns:
        int: The highest common sum achievable by removing elements from the top of the stacks
             to make them equal in height, or 0 if no common sum is found.

    Example:
        >>> equalStacks([3, 2, 1], [4, 1, 1], [1, 4, 1])
        4
    """
    sums = (stack_sums(h1), stack_sums(h2), stack_sums(h3))
    
    common_sums = set(sums[0]).intersection(*sums[1:])

    if common_sums:
        return max(common_sums)
    else:
        return 0



# Attempt 1:
# def reduce_tower(h):
#     h=h[1:]
#     return h
    
# def equalStacks(h1, h2, h3):
 
#     while sum(h1) != sum(h2) and sum(h2) != sum(h3):
#         max_sum = max(sum(h1), sum(h2), sum(h3))
#         if max_sum == sum(h1):
#             h1 = reduce_tower(h1)
#         elif max_sum == sum(h2):
#             h2 = reduce_tower(h2)
#         elif max_sum == sum(h3):
#             h3 = reduce_tower(h3)
    
#     return sum(h1)

# Attempt 2:
# def equalStacks(h1, h2, h3):
 
#     while sum(h1) != sum(h2) and sum(h2) != sum(h3):
#         stacks = [h1, h2, h3]
#         max_sum = float('-inf')
#         max_stack = None

#         for i in stacks:
#             current_sum = sum(i)
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 max_stack = i
        
#         del max_stack[0]
    
#     return sum(h1)

# Attempt 3:
# def h1h2_equal(h1, h2):
#     while sum(h1) != sum(h2):
#         if sum(h1) > sum(h2):
#             del h1[0]
#         else:
#             del h2[0]
#     return h1, h2
            
# def h2h3_equal(h2, h3):
#     while sum(h2) != sum(h3):
#         if sum(h3) > sum(h2):
#             del h3[0]
#         else:
#             del h2[0]
#     return h2, h3

# def equalStacks(h1, h2, h3):
    
#     while sum(h1) != sum(h2) and sum(h2) != sum(h3):
#         h1h2_equal(h1, h2)
#         h2h3_equal(h1, h2)

#     return sum(h1)

# Attempt 4:
# def equalStacks(h1, h2, h3):
 
#     while sum(h1) != sum(h2) and sum(h2) != sum(h3):
#         min_sum = min(sum(h1), sum(h2), sum(h3))
#         while sum(h1) > min_sum:
#             del h1[0]
#         while sum(h2) > min_sum:
#             del h2[0]
#         while sum(h3) > min_sum:
#             del h3[0]
        
#     return sum(h1)



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(str(result) + '\n')



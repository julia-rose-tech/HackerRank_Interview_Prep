#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Sample Input:
# 9
# 10 20 20 10 10 30 50 10 20

# Sample Output:
# 3


def sockMerchant(n, ar):
    
    unique_elements = set(ar)
    counts = [ar.count(i) for i in unique_elements]
  
    pairs = 0
    for i in counts:
        pairs += i//2
    return pairs

if __name__ == '__main__':
    

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

# CHATGPT suggestion:
# from collections import Counter

# def sockMerchant(n, ar):
#     # Use Counter to count occurrences of each color
#     color_counts = Counter(ar)
    
#     # Calculate the number of pairs for each color
#     pairs = sum(count // 2 for count in color_counts.values())
    
#     return pairs

# if __name__ == '__main__':
#     n = int(input().strip())
#     ar = list(map(int, input().rstrip().split()))
#     result = sockMerchant(n, ar)
#     print(result)
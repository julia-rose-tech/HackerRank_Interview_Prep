#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
# Mathematics:
# x+y = x XOR y + 2^(x&y) (Always true)

# Count how many zeros in the binary expression of the number, and the answer is 2 to the power of that count. 
# I.e 10 is 1010, so the answer is 2^2 = 4

# def sumXor(n):  ** This code is too slow ***
#     count = 0
#     for i in range(n+1):
#         if i+n == i^n:
#             print(str(i)+" and "+str(n))
#             count += 1
#     return count

def sumXor(n):
    count = 0
    while n > 0:
        if n & 1 == 0:  # Check if the least significant bit is unset (0).
            count += 1
        n >>= 1  # Right-shift n to the next bit.
    return 2 ** count




if __name__ == '__main__':

    n = int(input().strip())

    result = sumXor(n)

    print(str(result) + '\n')

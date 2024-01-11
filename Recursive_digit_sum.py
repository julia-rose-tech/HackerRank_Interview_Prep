#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
# Example, n = 9875 and k = 4, The answer is 8

def add_digits(string_n):
    total_sum = 0
    for char in string_n:
        total_sum += int(char)
    total_sum = total_sum
    return str(total_sum)
    
def superDigit(n, k):
    first_sum = int(add_digits(str(n)))*k
    super_string_n= str(first_sum)
    while len(super_string_n)>1:
        super_string_n = add_digits(super_string_n)
    return int(super_string_n)

if __name__ == '__main__':
    k = int(input().strip())
    n = int(input().strip())
    result = superDigit(n, k)
    print(result)


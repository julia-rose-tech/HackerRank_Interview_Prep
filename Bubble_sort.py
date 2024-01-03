#!/bin/python3

import math
import os
import random
import re
import sys

# SAMPLE INPUT:
# 7
# 4 9 5 0 8 3 4

# SAMPLE OUTPUT:

# [0, 3, 4, 4, 5, 8, 9]
# Array is sorted in 12 swaps.
# First Element: 0
# Last Element: 9

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    number_of_swaps = 0
    
    for i in range(0, n):
        
        for j in range(0, n-1):
            if a[j]>a[j+1]:
                temp_value = a[j]
                a[j] = a[j+1]
                a[j+1] = temp_value
                number_of_swaps += 1
        if number_of_swaps == 0:
            break
    print(a)
    print("Array is sorted in " + str(number_of_swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))
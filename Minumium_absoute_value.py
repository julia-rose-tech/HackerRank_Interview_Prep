#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_difference = abs(arr[n-1]-arr[0])

    for index_i in range(n-1):
        for index_j in range(index_i+1, n):
            if abs(arr[index_j]-arr[index_i]) < min_difference:
                min_difference = abs(arr[index_j]-arr[index_i])
                
    return(min_difference)

if __name__ == '__main__':


    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
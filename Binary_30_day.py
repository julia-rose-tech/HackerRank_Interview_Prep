#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

# STDIN       Function
# -----       --------
# 2           q = 2
# 3 10        A[] and B[] size n = 3, k = 10
# 2 1 3       A = [2, 1, 3]
# 7 8 9       B = [7, 8, 9]
# 4 5         A[] and B[] size n = 4, k = 5
# 1 2 2 1     A = [1, 2, 2, 1]
# 3 3 3 4     B = [3, 3, 3, 4]

# Output:
# YES
# NO

def twoArrays(k, A, B):
    sorted_A = sorted(A)
    sorted_B_descending = sorted(B, reverse=True)
    sums = []*len(A)
    all_greater = True
    for i in range(len(A)):
        sums.append(sorted_A[i] + sorted_B_descending[i])
        if sums[i] < k:
            all_greater = False
            break
    if all_greater is False:
        result = "NO"
    else:
        result = "YES"
    return (result)
            
        
        


q = int(input().strip())

for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = twoArrays(k, A, B)

    print(result)



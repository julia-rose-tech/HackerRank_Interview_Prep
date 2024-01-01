#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
matrix = [[112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108]]

def flippingMatrix(matrix):
    n = len(matrix)//2
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += max(matrix[i][j], matrix[i][~j], matrix[~i][j], matrix[~i][~j])
    return sum

# if __name__ == '__main__':

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         matrix = []

#         for _ in range(2 * n):
#             matrix.append(list(map(int, input().rstrip().split())))

result = flippingMatrix(matrix)

print(result)

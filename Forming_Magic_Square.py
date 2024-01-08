#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

# Information about 3 x 3 magic squares
# - The sum of each row and column is 15.
# - There are only 8 ways to sum up to 15 using the numbers 1-9, resulting in 8 possible magic squares.
# - Hence, as 5 is needed in four of these sums, the middle number must be 5.
# - Following similar logic, the corners must be 2, 4, 6, 7, and the edges must be the numbers 1, 3, 7, 9.

def formingMagicSquare(s):
    """
    This function calculates the minimum cost to convert a 3x3 matrix 's' into a magic square.

    :param s: A 3x3 matrix represented as a 2D list of integers.
    :return: An integer representing the minimum cost to form a magic square.
    """
    least_cost = float('inf')
    possible_magic_squares = [
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    ]
    for square in possible_magic_squares:
        cost = 0
        for i in range(len(s)):
            for j in range(len(square[i])):
                if s[i][j] != square[i][j]:
                    cost += abs(s[i][j] - square[i][j])
        if cost < least_cost:
            least_cost = cost
    return least_cost

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')

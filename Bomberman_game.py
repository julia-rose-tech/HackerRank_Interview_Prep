#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


grid =['.......', '...O...', '....O..','.......', 'OO.....', 'OO.....']

n = 7

    
def bombs_detotate(grid):
    r = len(grid)
    c = len(grid[0])
    for i in range(len(grid)):
        grid[i] = [char for char in grid[i]]
    detonated_grid = [['O' for _ in range(c)] for _ in range(r)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                detonated_grid[i][j] = '.'
                if i > 0:
                    detonated_grid[i-1][j] = '.'
                if i<len(grid)-1:
                    detonated_grid[i+1][j] = '.'
                if j > 0:
                    detonated_grid[i][j-1] = '.'
                if j<len(grid[i])-1:
                    detonated_grid[i][j+1] = '.'

    for i in range(len(detonated_grid)):
        detonated_grid[i] = ''.join(detonated_grid[i])
    return detonated_grid


def bomberMan(n, grid):
  
    r = len(grid)
    c = len(grid[0])


    if n == 1:
        return (grid)
    elif n % 2 == 0:
       return ['O' * c for _ in range(r)]
    elif n % 4 == 3:  
        return bombs_detotate(grid)
    elif n % 4 == 1:
        return bombs_detotate(bombs_detotate(grid))


print(bomberMan(n, grid))


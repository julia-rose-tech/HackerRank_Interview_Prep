#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
# Example Input:   
# 1
# 5      
# ebacd   
# fghij
# olmkn
# trpqs
# xywuv

def gridChallenge(grid):
    # Determine the number of rows in the grid
    j_range = len(grid)
    # Determine the number of columns in the grid
    n = len(grid[0])
    # Create a new grid to store sorted rows
    new_grid = []
    # Initialize a list to track whether columns are sorted alphabetically
    columns_sorted = [True] * n
    # Initialize a flag to check if all columns are sorted alphabetically
    alphabetical = True
    
    # Sort each row alphabetically and store in the new grid
    for i in grid:
        char_array = list(i)
        char_array.sort()
        new_grid.append(char_array)
    
    # Check if each column is sorted alphabetically
    for i in range(n):
        column_array = []
        for j in range(j_range):
            column_array.append(new_grid[j][i])
        column_array_sorted = sorted(column_array)
        if column_array != column_array_sorted:
            columns_sorted[i] = False
            break
            
    # Check if all columns are sorted alphabetically
    for i in range(n):
        if columns_sorted[i] is not True:
            alphabetical = False
    
    # Return "YES" if all columns are sorted alphabetically, otherwise return "NO"
    if alphabetical:
        return "YES"
    else:
        return "NO"
     

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    for t_itr in range(t):
        # Read the number of rows
        n = int(input().strip())

        grid = []

        # Read the grid rows
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        # Call the gridChallenge function and print the result
        result = gridChallenge(grid)

        print(result + '\n')

# CHATGPT suggestion: *Added Input validation

# #!/bin/python3

# # Constants for better readability
# YES = "YES"
# NO = "NO"

# def isGridAlphabeticallySorted(grid):
#     # Determine the number of rows in the grid
#     num_rows = len(grid)
    
#     if num_rows < 1:
#         return NO  # Empty grid cannot be alphabetically sorted
    
#     # Determine the number of columns in the grid
#     num_columns = len(grid[0])
    
#     # Check if all rows have the same length
#     if any(len(row) != num_columns for row in grid):
#         return NO  # Rows have different lengths
    
#     # Create a new grid with sorted rows
#     sorted_grid = [sorted(row) for row in grid]
    
#     # Check if all columns are sorted alphabetically
#     for i in range(num_columns):
#         column = [row[i] for row in sorted_grid]
#         if column != sorted(column):
#             return NO
    
#     return YES

# if __name__ == '__main__':
#     t = int(input().strip())

#     for _ in range(t):
#         n = int(input().strip())
#         grid = [input().strip() for _ in range(n)]

#         result = isGridAlphabeticallySorted(grid)
#         print(result)


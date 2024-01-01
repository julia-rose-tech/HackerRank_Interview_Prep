
#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# Sample Input:
# 1 1 2 2 3
# Output = 1

def migratoryBirds(arr):

    unique_birds = set(arr)

    counts = []

    for i in unique_birds:
        count_i = arr.count(i)
        counts.append([i, count_i])

    i_values = [element[1] for element in counts]
    max_i_value = max(i_values)

    for i, j in counts:
        if j == max_i_value:
            return (i)
            break


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

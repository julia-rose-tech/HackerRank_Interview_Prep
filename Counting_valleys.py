#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Sample Input:
# 8
# UDDDUDUU

# Sample Out put: 1

def countingValleys(steps, path):
    count = 0
    result = 0
    for i in path:
        if i == "U" and count == -1:
            count += 1
            result +=1
        elif i == "U":
            count += 1
        else:
            count -= 1
    return (result)


steps = int(input().strip())

path = input()

result = countingValleys(steps, path)
print(result)

# ChatGPT code suggestion:

# def countingValleys(steps, path):
#     count = 0  # Represents the current altitude
#     valleys = 0  # Represents the number of valleys

#     for step in path:
#         if step == "U":
#             count += 1
#             if count == 0:
#                 valleys += 1
#         else:  # Assuming only "U" and "D" characters in the path
#             count -= 1

#     return valleys

# # Read input
# steps = int(input().strip())
# path = input().strip()

# # Perform counting valleys
# result = countingValleys(steps, path)
# print(result)
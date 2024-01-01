#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    distance_diff = x2 - x1
    print(distance_diff)
    speed_diff = v2 - v1
    print(speed_diff)
    ans = "NO" #set ans = "NO" here to eliminate mulitple else clauses
    if speed_diff != 0:
        if distance_diff % speed_diff == 0:
            if distance_diff <0 or speed_diff <0:
                ans = "YES"
    #         else:
    #             ans = "NO"
    #     else:
    #         ans = "NO"
    # else:
    #     ans = "NO"
    return (ans)

# CHATGPT Suggestion:

# def kangaroo(x1, v1, x2, v2):
#     if v1 == v2:  # Kangaroos have the same speed, they'll either meet initially or never meet.
#         return "YES" if x1 == x2 else "NO"
    
#     # Calculate the time it takes for the kangaroos to meet (if they do).
#     t = (x2 - x1) / (v1 - v2)
    
#     # If t is a non-negative integer, the kangaroos will meet at that time.
#     if t >= 0 and t.is_integer():
#         return "YES"
#     else:
#         return "NO"


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)

print(result)

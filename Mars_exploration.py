#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Sample 0
# s = SOSSPSSQSSOR, and signal length = 12 . Sami sent  SOS messages (i.e.: ).

# Expected signal: SOSSOSSOSSOS
# Recieved signal: SOSSPSSQSSOR

# We print the number of changed letters, which is 3.

# Sample 1

#  = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

# Expected Signal: SOSSOS
# Received Signal: SOSSOT

# We print the number of changed letters, which is .

def marsExploration(s):
    changed_letters = 0
    original_signal = ['S', 'O', 'S'] * int(len(s)/3)

    for index_i, i in enumerate(original_signal):
        for index_j, j in enumerate(s):
            if index_i == index_j:
                if i != j:
                    changed_letters += 1
    return (changed_letters)


s = input()

result = marsExploration(s)

print(result)

# ChatGPT: 
# def marsExploration(s):
#     original_signal = 'SOS' * (len(s) // 3)
#     changed_letters = sum(c1 != c2 for c1, c2 in zip(original_signal, s))
#     return changed_letters

# s = input()
# result = marsExploration(s)
# print(result)
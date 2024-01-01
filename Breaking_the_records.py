#!/bin/python3

import math
import os
import random
import re
import sys

#
# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

# Sample Input
#   4
#   12 24 10 24

# Sample Output
#   (1, 1)   

def breakingRecords(scores):
    min_count=0
    max_count=0
    min_score=scores[0]
    max_score=scores[0]
    for i in range(1, n):
        if scores[i] > max_score:
            max_score = scores[i]
            max_count += 1
        elif scores[i] < min_score:
            min_score = scores[i]
            min_count += 1
    return (max_count, min_count)
            


n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# CThere is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

# Sample Input:
#     3
#     ab
#     ab
#     abc
#     3
#     ab
#     abc
#     bc
#Output = [2,1,0]


def matchingStrings(strings, queries):
    results = [0] * len(queries)
    for index_i, i in enumerate(queries):
        for j in (strings):
            if j == i:
                results[index_i] += 1

    return (results)



strings_count = int(input().strip())

strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)

print(res)
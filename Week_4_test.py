#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return(-1)
    else:
        changes = 0
        first_string = s[:len(s)//2]
        second_string = s[len(s)//2:]
        unique_first_string = list(set(first_string))
        for i in unique_first_string:
            count_1 = first_string.count(i)
            count_2 = second_string.count(i)
            if count_1 > count_2:
                changes += abs(count_2-count_1)
        return changes

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result) + '\n')


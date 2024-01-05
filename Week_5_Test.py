#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

sys.set_int_max_str_digits(0) #increases the limit for interger string conversion, default is 4300

def next_term(t1, t2):
    tn = t1 + (t2)**2
    return tn

def fibonacciModified(t1, t2, n):
    i = 0
    while i < (n-2):
        tn = next_term(t1, t2)
        t1 = t2
        t2 = tn
        i += 1
    return t2



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    print(str(result) + '\n')

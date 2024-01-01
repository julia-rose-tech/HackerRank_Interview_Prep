#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p

# Find the minimum number of page turns to get to page p, in a book with n pages. You can start from the back or front of the book. 
# Book page numbers are in the following pattern. -1 23 34 56 78....

def pageCount(n, p):
    if p <= (n / 2):
        number_turns = (p)/ 2
    else:
        if n % 2 == 0:
            number_turns = math.ceil((n - p)/2)
        else:
            number_turns = (n-p)/2
        
    return (int(number_turns))

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
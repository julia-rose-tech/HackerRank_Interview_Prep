#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# Find the unique value in the array
a = [1, 2, 3, 3, 4, 1, 2]

def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            print(i)
            break

lonelyinteger(a)
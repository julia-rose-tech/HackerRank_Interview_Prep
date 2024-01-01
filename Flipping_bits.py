# sample input = 
# 3
# 2147483647
# 1
# 0

# Sample output = 
# 2147483648
# 4294967294
# 4294967295


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    flipped_integers = []

    for i in n:
        # Change to 32 bits in binary
        thirty_two_bits = (format(i, '032b'))


        # Separate into individual characters
        digits = [int(digit_char) for digit_char in thirty_two_bits]

        # Flip the digits
        flipped_digits = []
        for digit in digits:
            if digit == 0:
                flipped_digits.append(digit + 1)
            elif digit ==1:
                flipped_digits.append(digit - 1)

        # Concatenate back into 32 bits
        flipped_bits =int(''.join(map(str, flipped_digits)), 2)

        # Change back to base 10 integers
        flipped_integers.append(flipped_bits)

    return flipped_integers
        


q = int(input().strip())
n_arr = []
for q_itr in range(q):
    n = int(input().strip())
    n_arr.append(n)


result = flippingBits(n_arr)

for i in result:
    print(i)


 

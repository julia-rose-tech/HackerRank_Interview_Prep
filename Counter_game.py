#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def find_matching_bin(n):
    """
    Find the largest power of 2 less than or equal to n and return it as an integer.

    :param n: A positive integer n.
    :return: The largest power of 2 less than or equal to n.
    """
    binary_n = format(n, 'b')
    length_binary_n = len(binary_n)
    matched_str = '1'+'0'*(length_binary_n-1)
    return int(matched_str)
    
def reduce_n(n):
    """
    Reduce the value of n by subtracting the largest power of 2 less than or equal to n.

    :param n: A positive integer n.
    :return: The reduced value of n after subtracting the largest power of 2.
    """
    binary_n = format(n, 'b')
    length_binary_n = len(binary_n)
    matched_str = '1'+'0'*(length_binary_n-1)
    reduced_binary_n = int(binary_n)-int(matched_str)
    reduced_n = int(str(reduced_binary_n), 2)
    return reduced_n
    
def counterGame(n):
    """
    Simulate the Counter Game and determine the winner (Richard or Louise).

    :param n: A positive integer n.
    :return: A string indicating the winner (Richard or Louise).
    """
    number_of_turns = 0
    while n > 1:
        if find_matching_bin(n) == int(format(n, 'b')):
            n = n // 2
            number_of_turns += 1
        else:
            n = reduce_n(n)
            number_of_turns += 1
    
    if number_of_turns % 2 == 0:
        return "Richard"
    else:
        return "Louise"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        print(result + '\n')



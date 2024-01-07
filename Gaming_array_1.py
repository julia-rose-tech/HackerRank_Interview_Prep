#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):

    """
    This function simulates a game where two players, Andy and Bob, take turns removing elements from an array.
    Each player can remove the maximum element from the array during their turn. The game continues until 
    there are no more elements to remove. The function determines the winner of the game, either "ANDY" or "BOB".

    :param arr: A list of integers representing the initial array.
    :return: A string indicating the winner of the game, either "ANDY" or "BOB".
    """

    number_of_turns = 0
    max_element = float('-inf')  # Initialize max_element with negative infinity
  
    for i in arr:
        if i > max_element:
            max_element = i
            number_of_turns += 1

    if number_of_turns % 2 == 0:
        return "ANDY"
    else:
        return "BOB"
    
if __name__ == '__main__':

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        print(result + '\n')

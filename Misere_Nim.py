#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as a parameter.
#

def misereNim(s):
    """
    This function implements the Misère Nim game, a variation of the traditional Nim game.
    
    In Misère Nim, there are several piles of stones, and two players take turns removing stones from a single pile.
    The player who removes the last stone loses the game. The game follows these rules:
    
    1. In each turn, a player can remove any number of stones (at least one) from a single pile.
    2. The player who takes the last stone loses if and only if the total number of stones across all piles is even.
    3. The player who takes the last stone wins if the total number of stones across all piles is odd.

    :param s: A list of integers representing the sizes of the piles.
    :return: A string indicating the winner of the game, either "First" or "Second".

    ~If all piles contain exactly one stone, then first player wins with an odd number of stones and second wins with an even number. ~Otherwise, we calculate the nimSum, which is found by running XOR on all sizes of piles ~If the nimSum is zero, second player wins. If not, first player wins.
    """

    XOR = s[0]
    sum = s[0]
    for i in s[1:]:
        XOR = XOR ^ i
        sum = sum + i
    if sum == len(s):
        if sum % 2 == 0:
            return ("First")
        else:
            return ("Second")
    else:
        if XOR == 0:
            return ("Second")
        else:
            return ("First")

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        print(result + '\n')

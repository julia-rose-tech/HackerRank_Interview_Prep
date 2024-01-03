#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n = number of towers
#  2. INTEGER m = height of tower

#All towers always have the same height, so a player can always mirror the move of the other player.

# Therefore, if the number of towers are even, then P2 always have the strategy to mirror the moves made by P1, leaving P1 to loose. If the height of tower is 1, then P1 always lose immediately, so P2 is also the winner.

# If the number of towers are odd, then P1 can reduce a tower to 1, then after P2 makes a move, P1 always mirrors the moves made by P2, leaving P2 to lose. (This includes the case where there is only 1 tower).

number_of_moves_left = 0

def towerBreakers(n, m):
    
    if m  == 1 or n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
   
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        print(result)
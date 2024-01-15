#!/bin/python3

import math
import os
import random
import re
import sys

# The minimumBribes function calculates the minimum number of bribes required to arrange the queue correctly.
# It takes an integer array 'q' as input, representing the current state of the queue.

def minimumBribes(q):
    minBribes = 0

    # Loop through the queue in reverse order
    for i in range(len(q), 0, -1):
        if i != q[i-1]:
            # If the current person bribed once and is now in the correct position
            if i == q[i-2]:
                q[i-2], q[i-1] = q[i-1], q[i-2]  # Swap positions
                minBribes += 1
                print(q)  # Print the updated queue after a swap

            # If the current person bribed twice and is now in the correct position
            elif i == q[i-3]:
                q[i-3], q[i-2], q[i-1] = q[i-2], q[i-1], q[i-3]  # Swap positions
                minBribes += 2
                print(q)  # Print the updated queue after two swaps

            # If the current person has bribed more than twice, return "Too chaotic"
            else:
                return "Too chaotic"

    return minBribes

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))

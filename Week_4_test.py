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
    """
    Calculate the minimum number of changes needed to make two halves of a string anagrams of each other.

    Args:
    s (str): The input string to be analyzed.

    Returns:
    int: The minimum number of changes required to make two halves of the string anagrams.
         Returns -1 if the length of the input string is odd and cannot be split evenly.
    """

    # Check if the length of the input string is odd
    if len(s) % 2 != 0:
        return -1  # Cannot split an odd-length string into two equal parts

    # Initialize a variable to keep track of changes needed
    changes = 0

    # Split the input string into two equal halves
    first_string = s[:len(s)//2]
    second_string = s[len(s)//2:]

    # Create a set of unique characters in the first half of the string
    unique_first_string = list(set(first_string))

    # Iterate through unique characters in the first half
    for i in unique_first_string:
        count_1 = first_string.count(i)  # Count of the character in the first half
        count_2 = second_string.count(i)  # Count of the character in the second half

        # If there are more occurrences in the first half, add the difference to changes
        if count_1 > count_2:
            changes += abs(count_2 - count_1)

    return changes  # Return the total number of changes required

if __name__ == '__main__':
    q = int(input().strip())  # Number of test cases

    for q_itr in range(q):
        s = input()  # Input string for each test case

        result = anagram(s)  # Call the anagram function to get the result

        print(str(result) + '\n')  # Print the result for each test case

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as a parameter.
#

def superReducedString(s):
    """
    Removes adjacent duplicate characters from a given string 's'.

    Args:
        s (str): The input string from which adjacent duplicates are removed.

    Returns:
        str: The modified string with adjacent duplicates removed, or 'Empty String'
             if the resulting string is empty.

    Example:
        Input: "aaabccddd"
        Output: "abd"

    Note:
        The function iterates through the string, removing adjacent duplicate
        characters until no more duplicates are found. If the resulting string
        is empty, it returns 'Empty String'.
    """
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1

    if len(s) == 0:
        return "Empty String"
    else:
        return s

if __name__ == '__main__':
    s = input()
    result = superReducedString(s)
    print(result + '\n')


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def is_pair(char1, char2):
    pair = False
    if ord(char1) == 40 and ord(char2) == 41:
        pair = True
    # if ord(char1) == 41 and ord(char2) == 40:
    #     pair = True
    if ord(char1) == 123 and ord(char2) == 125:
        pair = True
    # if ord(char1) == 123 and ord(char2) == 123:
    #     pair = True
    if ord(char1) == 91 and ord(char2) == 93:
        pair = True
    # if ord(char1) == 93 and ord(char2) == 91:
    #     pair = True
    return pair

    

def isBalanced(s):

    # if len(s)//2 != 0:
    #     return "NO"

    i = 0
    while i < len(s) - 1:
        if is_pair(s[i], s[i + 1]) is True:
            s = s[:i] + s[i + 2:]
            if i > 0:
                i -= 1
        else:
            i += 1

    if len(s) == 0:
        return "YES"
    else:
        return "NO"


  
    
s = "{]}"
s1 = "{[()]}"
s2 = "{(([])[])[]]}"
s3 = "{(([])[])[]}[]"
s4 = "{{([])}}"
# Ans = NO YES NO YES YES

print(isBalanced(s2))

# if __name__ == '__main__'

#     t = int(input().strip())

#     for t_itr in range(t):
#         s = input()

#         result = isBalanced(s)

#         print(result + '\n')



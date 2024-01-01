#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    lowercase_alphabet = list(string.ascii_lowercase)
    uppercase_alphabet = list(string.ascii_uppercase)
    new_array = []
    regex_metacharacters = r".*+?|[](){}\\"
    for i in s:
        match_meta = re.search(i, regex_metacharacters)
        if match_meta:
            new_array.append(i)
        else:
            match_lower = re.search(i, string.ascii_lowercase)
            if match_lower:
                new_index = match_lower.start()+k
                if new_index >= 25:
                    new_index = new_index % 26
                new_array.append(lowercase_alphabet[new_index])
            else:
                match_upper = re.search(i, string.ascii_uppercase)
                if match_upper:
                    new_index = match_upper.start()+k
                    if new_index >= 25:
                        new_index = new_index % 26
                    new_array.append(uppercase_alphabet[new_index])
                else:
                    new_array.append(i)
    return(''.join(new_array))


# More efficient code from CHATGPT: (import string not required)

# def caesarCipher(s, k):
#     new_array = []

#     for char in s:
#         if char.isalpha():
#             if char.islower():
#                 new_index = (ord(char)-ord('a')+k) % 26
#                 new_char = chr(ord('a')+new_index)
#             else:
#                 new_index = (ord(char)-ord('A')+k) % 26
#                 new_char = chr(ord('A')+new_index)
#             new_array.append(new_char)
#         else:
#             new_array.append(char)
#     return ''.join(new_array)
          



if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)

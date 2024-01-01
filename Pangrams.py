#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'pangrams' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# Sample Input 0
# We promptly judged antique ivory buckles for the next prize
# Sample Output 0
# pangram

# Sample Input 1
# We promptly judged antique ivory buckles for the prize
# Sample Output 1
# not pangram
#[there is no x]


def pangrams(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_count = [0]*26

    for i in s:
        for index_j, j in enumerate(alphabet):
            if i.lower() ==j:
                alphabet_count[index_j] +=1

    if all(i > 0 for i in alphabet_count):
        result = print("pangram")
    else:
        result = print("not pangram")
    return (result)

s = input()
result = pangrams(s)

# ChatGPT suggestion:
# def pangrams(s):
#     # Convert the input string to lowercase and remove non-alphabetic characters
#     cleaned_s = ''.join(char.lower() for char in s if char.isalpha())

#     # Use set to get unique letters and check if it's a pangram
#     if set(cleaned_s) == set('abcdefghijklmnopqrstuvwxyz'):
#         result = "pangram"
#     else:
#         result = "not pangram"

#     print(result)
#     return result

# # Example usage
# s = input()
# result = pangrams(s)
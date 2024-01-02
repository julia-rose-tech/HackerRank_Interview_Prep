#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# Define the characters used for checking password requirements
numbers = "0123456789"
special_characters = "!@#$%^&*()-+"

def minimumNumber(n, password):
    """
    Calculate the minimum number of characters to add to a password to meet certain requirements.

    Args:
    n (int): The length of the password.
    password (str): The input password.

    Returns:
    int: The minimum number of characters to add to meet the requirements.
    """

    answer = 0
    one_lower_case = False
    one_digit = False
    one_upper_case = False
    one_special_char = False

    for char in password:
        if char.islower():
            one_lower_case = True
        if char.isupper():
            one_upper_case = True
        if char in special_characters:
            one_special_char = True
        if char in numbers:
            one_digit = True

    if one_lower_case is False:
        answer += 1

    if one_special_char is False:
        answer += 1

    if one_upper_case is False:
        answer += 1

    if one_digit is False:
        answer += 1

    if n + answer < 6:
        answer += abs(n + answer - 6)
    
    return answer
        

if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')

#CHATGPT suggestion: Using re
    
    #!/bin/python3

# import re

# def minimumNumber(n, password):
#     """
#     Calculate the minimum number of characters to add to a password to meet certain requirements.

#     Args:
#     n (int): The length of the password.
#     password (str): The input password.

#     Returns:
#     int: The minimum number of characters to add to meet the requirements.
#     """

#     answer = 0

#     # Check for at least one lowercase letter, uppercase letter, special character, and digit using regular expressions
#     if not re.search(r'[a-z]', password):
#         answer += 1
#     if not re.search(r'[A-Z]', password):
#         answer += 1
#     if not re.search(r'[!@#$%^&*()-+]', password):
#         answer += 1
#     if not re.search(r'[0-9]', password):
#         answer += 1

#     # If the password is shorter than 6 characters, add characters to meet the minimum length
#     if n + answer < 6:
#         answer += abs(n + answer - 6)
    
#     return answer

# if __name__ == '__main__':
#     n = int(input().strip())
#     password = input()

#     answer = minimumNumber(n, password)

#     print(answer)


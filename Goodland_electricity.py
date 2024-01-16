
#!/bin/python3

import math
import os
import random
import re
import sys

def pylons(k, arr):
    """
    Calculate the maximum number of pylons that can be powered given constraints.

    Parameters:
    - k: An integer representing the maximum distance between pylons that can be powered.
    - arr: A list of integers representing the availability of pylons (1 for powered, 0 for unpowered).

    Returns:
    - The maximum number of pylons that can be powered while satisfying the constraints, or -1 if it's not possible.
    """

    # Initialize indices for the leftmost and rightmost pylons within range.
    i = 0
    while i <= k - 1:
        if arr[i] == 0:
            if i == k - 1:
                return -1
            else:
                i += 1
        else:
            break

    j = len(arr) - 1
    while j >= len(arr) - k:
        if arr[j] == 0:
            if j == len(arr) - k:
                return -1
            else:
                j -= 1
        else:
            break

    passed_end_of_array = 0
    number_of_plants = 0
    index = k - 1
    number_of_zeros = 0

    # Traverse the array to calculate the maximum number of powered pylons while satisfying constraints.
    while index < len(arr):
        if number_of_zeros == k * 2 - 1:
            number_of_plants = -1
            break
        if arr[index] == 1:
            number_of_zeros = 0
            number_of_plants += 1

            if len(arr) - index <= k:
                break
            # Move the index to the next reachable pylon position.
            index = index + k * 2 - 1
            if passed_end_of_array > 1:
                break
            # Check if the end of the array has been passed.
            if index > len(arr) - 1:
                index = len(arr) - 1
                passed_end_of_array = 1
        else:
            index -= 1
            number_of_zeros += 1

    return number_of_plants

# Sample input
k = 10
input_string = "1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0"

arr = list(map(int, input_string.split()))

# Call the function and print the result
print(pylons(k, arr))

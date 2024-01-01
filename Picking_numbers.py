

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

# Sample Output:
# a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
# answer = 5

# a = [4, 6, 5, 3, 3, 1]
# answer = 3

#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys

# Define a function called 'pickingNumbers'
def pickingNumbers(a):
    # Sort the input list 'a'
    sorted_a = sorted(a)

    # Initialize a list to store the lengths of consecutive subsequences
    array_lengths = []

    # Iterate through the sorted list 'sorted_a'
    for index_i, i in enumerate(sorted_a):
        array = [i]  # Initialize a subsequence with the current element
        for index_j, j in enumerate(sorted_a[index_i+1:]):
            if j <= array[0] + 1:
                array.append(j)  # Extend the subsequence if the next element is within 1 of the current element
            else:
                break  # Stop extending the subsequence when the next element is not within 1 of the current element
        array_length = len(array)
        array_lengths.append(array_length)

    # Find the maximum subsequence length
    max_sub_seq = max(array_lengths)

    # Print the maximum subsequence length
    print(max_sub_seq)

# Example usage of the 'pickingNumbers' function
if __name__ == '__main__':
    # Input the length of the list 'a'
    n = int(input().strip())

    # Input the elements of the list 'a'
    a = list(map(int, input().rstrip().split()))

    # Call the 'pickingNumbers' function with the list 'a'
    pickingNumbers(a)

    
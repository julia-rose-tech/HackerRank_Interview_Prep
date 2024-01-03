
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n: The number of sequences.
#  2. 2D_INTEGER_ARRAY queries: An array of queries, where each query is represented as a list [type, x, y].

def dynamicArray(n, queries):
    """
    Perform dynamic array operations based on the given queries.

    Args:
    n (int): The number of sequences.
    queries (list): A list of queries, where each query is represented as a list [type, x, y].
                    - type: The type of query (1 or 2).
                    - x: An integer parameter for query type 1.
                    - y: An integer parameter for query type 2.

    Returns:
    list: A list of integers representing the answers for query type 2.

    Note:
    This function implements a dynamic array where you can append elements to sequences based on queries
    of type 1 and retrieve values from sequences based on queries of type 2.

    Usage example:
    n = 2
    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0]]
    result = dynamicArray(n, queries)
    print(result)  # Output: [7, 3]

    **Important Note: Be cautious about using arr = [[]]*n; it may not work as intended.
    If you want a list of independent sublists, use arr = [[] for _ in range(n)] instead.
    """
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for q in queries:
        idx = ((q[1] ^ lastAnswer) % n)
        if q[0] == 1:
            arr[idx].append(q[2])
        elif q[0] == 2:  
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            answers.append(lastAnswer)
   
    return answers

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))

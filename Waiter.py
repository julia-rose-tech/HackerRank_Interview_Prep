#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def next_prime(n):
    is_prime = False
    n += 1
    while not is_prime:
        if n !=2 and n % 2 == 0:
            n += 1
        else:
            j = math.ceil(math.sqrt(n))
            if j % 2 == 0:
                j -= 1
            is_prime = True
            k = 3
            while k <= j : 
                if n % k == 0:
                    is_prime = False
                    n += 1
                    break
                else:
                    k += 2
    return n

class Stack:
    def __init__(self):
        self.stack = []

    def pushCharacter(self, char):
        self.stack.append(char)
 
    def popCharacter(self):
        char = self.stack.pop() if self.stack else None
        return (char)
        

def waiter(number, q):
    ith_prime = 2
    answers = []
    remainder_stack = Stack()
    
    for n in number:
        remainder_stack.pushCharacter(n)

    for i in range(q):
        indices_to_pop = []
    
        for n in range(len(remainder_stack.stack)):
            element = remainder_stack.stack[-(n+1)]
            if element % ith_prime == 0:
                answers.append(element)
                indices_to_pop.append(-(n+1))


        print(indices_to_pop)

        for j in reversed(indices_to_pop): 
            remainder_stack.stack.pop(j)
        print(remainder_stack.stack)


        ith_prime = next_prime(ith_prime)
    
    while len(remainder_stack.stack) > 0:
        answers.append(remainder_stack.stack[0])
        remainder_stack.stack.pop(0)

    print("Answers"+str(answers))
    
    return answers
       
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print(result)
    # print('\n'.join(map(str, result)))

# Sample Input:
# 5 1
# 3 4 7 6 5
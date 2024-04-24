import math

def next_prime(n):
    """
    Finds the next prime number greater than n.

    Parameters:
    - n (int): The number for which to find the next prime.

    Returns:
    - int: The next prime number greater than n.
    """
    is_prime = False
    n += 1
    while not is_prime:
        if n != 2 and n % 2 == 0:
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
    """
    Implementation of a stack data structure.
    """
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def pushCharacter(self, char):
        """
        Pushes a character onto the stack.

        Parameters:
        - char: The character to be pushed onto the stack.
        """
        self.stack.append(char)
    
    def popCharacter(self):
        """
        Pops a character from the stack.

        Returns:
        - char: The character popped from the stack.
        """
        char = self.stack.pop() if self.stack else None
        return char
    
def waiter(number, q):
    """
    Performs the waiter algorithm.

    Parameters:
    - number (list): The list of integers to be processed.
    - q (int): The number of iterations.

    Returns:
    - list: The list of integers after processing.
    """
    prime = 2
    answers = []
    working_stack = Stack()
    for num in number:
            working_stack.pushCharacter(num)

    for i in range(q):

        divisible_stack = Stack()
        non_divisible_stack = Stack()

        for j in range(len(working_stack.stack)):
            x = working_stack.popCharacter()
            if x % prime == 0:
                divisible_stack.pushCharacter(x)
            else:
                non_divisible_stack.pushCharacter(x)

        for k in range(len(divisible_stack.stack)):
            answers.append(divisible_stack.popCharacter())
        
        working_stack.stack = non_divisible_stack.stack

        prime = next_prime(prime)

    while len(working_stack.stack) > 0:
        answers.append(working_stack.popCharacter())

    return answers

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print(result)

# Sample Input:
# 5 1
# 3 4 7 6 5

from collections import deque

class Solution:
    """
    A class representing a solution for handling queue operations.
    
    Attributes:
        queue (deque): A deque object representing the queue.
    """
    
    def __init__(self):
        """
        Initializes the Solution object with an empty deque as the queue.
        """
        self.queue = deque()
        
    def enqueueCharacter(self, char):
        """
        Enqueues a character into the queue.

        Parameters:
            char (any): The character to be enqueued.
        """
        self.queue.append(char)
        
    def dequeueCharacter(self):
        """
        Dequeues a character from the queue.

        Returns:
            any: The dequeued character if the queue is not empty, otherwise None.
        """
        return self.queue.popleft() if self.queue else None
    
    def printFirstElement(self):
        """
        Retrieves the first character in the queue without dequeuing it.

        Returns:
            any: The first character in the queue if the queue is not empty, otherwise None.
        """
        return self.queue[0] if self.queue else None


def queue_solution(query_number, data):
    """
    Performs the queue operations based on the given query number and data.

    Parameters:
        query_number (int): The query number representing the type of operation.
        data (list): The data associated with the query.

    Returns:
        None
    """
    if query_number == 1:
        queue.enqueueCharacter(data)
    elif query_number == 2:
        queue.dequeueCharacter()
    else:
        print(*queue.printFirstElement())

# Main program
T = int(input().strip())
queue = Solution()
for T_itr in range(T):
    arr = list(map(int, input().rstrip().split()))
    query_number = arr[0]
    data = arr[1:]
    queue_solution(query_number, data)




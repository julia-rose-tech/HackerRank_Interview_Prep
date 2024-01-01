# Define a custom exception class called MyCustomError
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Define a Calculator class
class Calculator:
    def power(self, n, p):
        """
        Calculate n raised to the power of p.

        Parameters:
        n (int): The base.
        p (int): The exponent.

        Returns:
        int: The result of n raised to the power of p.

        Raises:
        MyCustomError: If n or p is a negative number.
        """
        if n < 0 or p < 0:
            raise MyCustomError("n and p should be non-negative")
        else:
            answer = n ** p
        return answer

# Create an instance of the Calculator class
myCalculator = Calculator()

# Input the number of test cases (T)
T = int(input())

# Process each test case
for i in range(T):
    # Input the values of n and p for each test case
    n, p = map(int, input().split())
    try:
        # Calculate n raised to the power of p using the Calculator's power method
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        # Handle exceptions, including MyCustomError, and print the error message
        print(e)



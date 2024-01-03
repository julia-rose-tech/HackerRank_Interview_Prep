import math

# List of numbers
num = [1, 2, 7, 169, 14, 35, 48, 21, 914, 784]

# Function to check if a number is a "smart number"
# A "smart number" is a square number (a number that is the square of an integer).
# Square numbers have an odd number of factors, so they are considered "smart."
def is_smart_number(i):
    # Calculate the integer square root of the number
    val = int(math.sqrt(i))
    # Check if the number is a square number
    if (i / val) == val:
        return True
    return False

# Loop through the list of numbers and determine if each one is a "smart number"
for i in num:
    ans = is_smart_number(i)
    if ans:
        print("YES")
    else:
        print("NO")

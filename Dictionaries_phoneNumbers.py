# Sample Input

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

# Sample Output
# sam=99912222
# Not found
# harry=12299933

import sys

n = int(input().strip())

phoneNumbers =  {}

for _ in range(n):
    inputs = input().strip().split(' ')
    name = inputs[0]
    phoneNumber = inputs[1]
    phoneNumbers.update({name: phoneNumber})

for line in sys.stdin:
    query = line.strip()
    try:
        phoneNumber = phoneNumbers[query]
        print(phoneNumber)
    except KeyError:
        print("Not found")

#Better version in ChatGPT:


# Read the number of entries
n = int(input().strip())

# Use a dictionary comprehension to create the phoneNumbers dictionary
phoneNumbers = {input().strip().split()[0]: input().strip().split()[1] for _ in range(n)}

# Query the dictionary using sys.stdin
for line in sys.stdin:
    query = line.strip()
    phoneNumber = phoneNumbers.get(query, "Not found")
    print(f"{query}={phoneNumber}")
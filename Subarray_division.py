
s = [4]
d = 4
m = 1

# s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
# d = 18
# m = 7


# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2

# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

count = 0
segments = []

for i in range(len(s)-(m-1)): 
    segment = 0   
    for j in range(m):      
        segment = segment+s[j+i]   
    segments.append(segment)
print(segments)
for i in segments:
    if i == d:
        count += 1


print(count)
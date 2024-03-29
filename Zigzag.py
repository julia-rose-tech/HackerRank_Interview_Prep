# Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and the last  elements are in decreasing order, where k = n+1/2. You need to find the lexicographically smallest zig zag sequence of the given array.

# a = [2, 3, 5, 1, 4]
# n = 5


n = 7
a = [1, 2, 3, 4, 5, 6, 7]

# n = 9
# a = [1, 4, 8, 3, 5, 9, 13, 14, 11]

def findZigZagSequence(a, n):
    a.sort()
    mid = int(((n + 1)/2)-1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# test_cases = int(input())
# for cs in range (test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
findZigZagSequence(a, n)
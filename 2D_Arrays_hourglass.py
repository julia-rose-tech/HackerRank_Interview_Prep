# Sample Input:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample output = 19

# Find the max value of the sum on the values in the shape of an hourglass for a 6x6 matrix. I.e:
# a b c
#   d  
# e f g 

import re
import sys

if __name__ == '__main__':

    arr = []
    
    hour_glass_sums = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for i in range(4):
        for j in range(4):
            # hour_glass_sum = arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2] CODE FOR FIRST HOURGLASS
            hour_glass_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            hour_glass_sums.append(hour_glass_sum)
    print(max(hour_glass_sums))
                
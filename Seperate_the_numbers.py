# Sample Input:
# 7
# 1234
# 91011
# 99100
# 101103
# 010203
# 13
# 1

# Sample Output:
# YES 1
# YES 9
# YES 99
# NO
# NO
# NO
# NO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
s = "12345678"


new_array = []
remaining_array = []

for i in range(1, len(s)//2+1):
    first_number = s[:i]
    previous_number = first_number
    for j in range(1, len(s)+1):
        current_number = s[(j-1)*i:j*i]
        if j>1 and int(previous_number)+1 != int(current_number):
            break
        else:
            print(current_number)
        previous_number = current_number
        
        
    # if int(first_number)+1 != int(next_number):
    #     break
            




  




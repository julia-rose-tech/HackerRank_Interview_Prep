

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.



def isValid(s):

    # Convert s string into array
    array_s = [char for char in s]
    # Create list of unique elements in array
    unique_array = list(set(array_s))
    # Create an array of the counts of each unique element (sorted)
    counts = sorted([array_s.count(i) for i in unique_array])
    # Count of how many elements deleted to create sherlock pattern
    one_subtracted = 0
    # Set answer to yes
    is_sherlock = "YES"


    # If single element, return yes
    if len(array_s) == 1:
        return "YES"
    
    # If there is a single 'one' in the counts array, delete it
    if counts[0] == 1:
        if counts[1] != 1:
            del counts[0]
            one_subtracted += 1

    # Set check_count, the first element in the array to which all other elements will be compared
    check_count = counts[0]      

    for index_i,i in enumerate(counts[:len(counts)]):
        # Check if i is larger than check_count
        # 'i' cannot be smaller as the array was sorted. If they are equal the loop will continue. 
        # if i is only larger by one unit, delete this unit and add 1 to one_subtracted, else break and set is_Sherlock to NO.
        if i > check_count:
            if i-1 == check_count:
                one_subtracted += 1
                counts[index_i] = check_count 
            else:
                is_sherlock = "NO"
                break

    # if more than one element was deleted to make this a sherlock pattern, return no. 
    if one_subtracted > 1:
          is_sherlock = "NO"

    return is_sherlock


s = "aabbac"



print(isValid(s))

   


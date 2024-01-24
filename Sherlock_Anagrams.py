#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Example: s = "MOM", answer = 2. MM = MM and OM = MO

# The list of all anagrammatic pairs is  at positions  respectively.

s = "kkkk" 
# answer = 10

def sherlockAndAnagrams(s):
    #create empty dictionary
    string_dict = {}
    # create count
    anagram_count = 0

    # splits string into arrays of increasing size, jumping up one character at a time
    # i is the length of the splice
    # the splice is "sorted" before added to the dictionary
    for i in range(1, len(s)+1):
        first_substring = str(''.join(sorted(s[:i])))
        remaining = s[1:]
        string_dict[first_substring] = 1
        # while within the size of the original string, keep splicing and adding to the dictionary
        while len(remaining) >= i:
            # if the splice is already present in the dictionary, increase the dictionary count by 1
            # add the dictionary count to our anagram count
            # only splices with a count greater than 1 will be added
            current_substring = str(''.join(sorted(remaining[:i])))
            remaining = remaining[1:]
            if current_substring in string_dict:
                anagram_count += string_dict[current_substring]
                string_dict[current_substring] += 1
            else:
                string_dict[current_substring] = 1
    print(string_dict)
    return anagram_count
            
    
           
print(sherlockAndAnagrams(s))

# if __name__ == '__main__':ß


#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = sherlockAndAnagrams(s)

#         print(str(result) + '\n')


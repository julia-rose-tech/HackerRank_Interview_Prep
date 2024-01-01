#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from 1 to 100.
# Any  less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of the grade is less than 38, no rounding occurs as the result will still be a failing grade.

# Sample Input: (Starts with number of grades)
# 4
# 73
# 67
# 38
# 33

# Sample Output:
# 75
# 67
# 40
# 33

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        unit_digit = grade % 10
        if grade > 37:
            if unit_digit == 3 or unit_digit == 8:
                rounded_grades.append(grade + 2)
            elif unit_digit == 4 or unit_digit == 9:
                rounded_grades.append(grade + 1)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    print(rounded_grades)

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

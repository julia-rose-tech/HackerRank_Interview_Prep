#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys

# Get input from the user
S = input()

# Attempt to convert the input to an integer
try:
    print(int(S))  # If successful, print the integer
except ValueError:
    print("Bad String")  # If a ValueError occurs (input cannot be converted to an integer), print an error message

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time. Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock. - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):

    char_array = list(s)
    hh = "".join(char_array[0:2])
    mm = "".join(char_array[3:5])
    ss = "".join(char_array[6:8])
    daytime = "".join(char_array[8:10])

    if daytime == "PM" and hh != "12":
        hh = str(int(hh) + 12)
    elif daytime == "AM" and hh == "12":
        hh = "00"

    twenty_four_hour_time = f"{hh}:{mm}:{ss}"
    return twenty_four_hour_time


s = input()

result = timeConversion(s)

print(result)

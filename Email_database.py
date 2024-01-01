#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    email_address = {}
    
    result = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        split_email = emailID.split("@")
        provider = split_email[1]
        email_address.update({"firstName": firstName, "emailID": emailID, "provider": provider})
        if provider == "gmail.com":
            result.append(firstName)
        
    sorted_result = sorted(result)
    for i in sorted_result:
        print(i)


# CHATGPT suggestion:
# if __name__ == '__main__':
#     num_entries = int(input().strip())
#     user_data = []

#     for _ in range(num_entries):
#         first_name, email_id = input().rstrip().split()
#         provider = email_id.split("@")[1]
#         user_data.append({"first_name": first_name, "email_id": email_id, "provider": provider})

#     # Filter users with "gmail.com" email addresses and sort by first name
#     gmail_users = sorted([user["first_name"] for user in user_data if user["provider"] == "gmail.com"])

#     for name in gmail_users:
#         print(name)

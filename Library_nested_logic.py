# Sample Input:
# 9 6 2015
# 6 6 2015

# Expected output:
# 45

# Sample Output:
# 31 12 2009
# 1 1 2010
# Expected Output:
# 0

def library_fine(date_returned, date_due):
    fine = 0
    if date_due[2] < date_returned[2]: #if date_due year < date_returned year set fine
        fine = 10000
    elif date_due[2] == date_returned[2]: #else if date_due year = date_returned year 
        if date_due[1] < date_returned[1]: # if date_due month > date_returned month set fine
            fine = (date_returned[1] - date_due[1])*500
        elif date_due[1] == date_returned[1]: #else if date_due month = date_returned month 
            if date_due[0] < date_returned[0]: #if date_due day <= date_returned day set fine 
                    fine = (date_returned[0] - date_due[0])*15
    return(fine)

if __name__ == '__main__':

    date_returned = list(map(int, input().rstrip().split()))

    date_due = list(map(int, input().rstrip().split()))

    result = library_fine(date_returned, date_due)

    print(result)
    
# CHATGPT Suggestion:

# def library_fine(date_returned, date_due):
#     fine = 0

#     if date_returned[2] > date_due[2]:  # Check year first
#         fine = 10000
#     elif date_returned[2] == date_due[2]:  # Check month
#         if date_returned[1] > date_due[1]:
#             fine = (date_returned[1] - date_due[1]) * 500
#         elif date_returned[1] == date_due[1]:  # Check day
#             if date_returned[0] > date_due[0]:
#                 fine = (date_returned[0] - date_due[0]) * 15

#     return fine

# if __name__ == '__main__':
#     date_returned = list(map(int, input().rstrip().split()))
#     date_due = list(map(int, input().rstrip().split()))
#     result = library_fine(date_returned, date_due)
#     print(result)
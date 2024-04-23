if __name__ == '__main__':

    t = int(input())
    S = str()
    versions = [""]

    for t_itr in range(t):
        n = str(input())
        q = int(n[0])
        data = n[1:].strip()
        if q == 1:
            S += data
            versions.append(S)
        elif q == 2:
            S = S[:-int(data)]
            versions.append(S)
        elif q == 3:
            index = int(data)-1
            print(S[index])
        elif q == 4:
            versions.pop()
            S = versions[-1]
        else:
            print ("Error")

#This code works, but failed the time limit
# if __name__ == '__main__':

#     t = int(input().strip())
#     S = str()
#     versions = [""]

#     for t_itr in range(t):
#         n = str(input())
#         q = int(n[0])
#         data = n[1:].strip()
#         if q == 1:
#             S += data
#             versions.append(S)
#         elif q == 2:
#             S = S[:(len(S)-int(data))]
#             versions.append(S)
#         elif q == 3:
#             print(S[int(data)-1:int(data)])
#         elif q == 4:
#             versions = versions[:-1]
#             S = versions[-1]
#         else:
#             print ("Error")


# CHATGPT suggestion:
# if __name__ == '__main__':
#     t = int(input().strip())
#     versions = [""]
#     current_version = ""

#     for _ in range(t):
#         query = input().strip().split()
#         q = int(query[0])

#         if q == 1:
#             data = query[1]
#             current_version += data
#             versions.append(current_version)
#         elif q == 2:
#             data = int(query[1])
#             current_version = current_version[:-data]
#             versions.append(current_version)
#         elif q == 3:
#             index = int(query[1]) - 1
#             if 0 <= index < len(current_version):
#                 print(current_version[index])
#             else:
#                 print("Index out of range")
#         elif q == 4:
#             if len(versions) > 1:
#                 versions.pop()
#                 current_version = versions[-1]
#             else:
#                 print("No previous version available")
#         else:
#             print("Invalid query")

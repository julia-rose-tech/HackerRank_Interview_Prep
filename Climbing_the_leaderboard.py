#!/bin/python3

import math
import os
import random
import re
import sys

# Following method was too slow:
def find_ranking(scores_array, new_score):
    ranking = 1
    for index_i, i in enumerate(scores_array):
        if index_i > 0:
            if i  != scores_array[index_i-1]:
                ranking += 1 
        if i == new_score:
            return ranking
    return ranking

    
def climbingLeaderboard(ranked, player):  
    rankings = []
    for new_score in player:
        index_to_insert = 0
        while index_to_insert < len (ranked) and ranked[index_to_insert] > new_score:
            index_to_insert += 1
        ranked.insert(index_to_insert, new_score)
        current_ranking = find_ranking(ranked, new_score)
        rankings.append(current_ranking)
    return rankings


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

print(climbingLeaderboard(ranked, player))

# ChatGPT faster method:
# def climbingLeaderboard(ranked, player):
#     unique_ranked = list(dict.fromkeys(ranked))  # Remove duplicates from ranked
#     print(unique_ranked)
#     rankings = []

#     i = len(unique_ranked) - 1  # Start from the last rank

#     for new_score in player:
#         while i >= 0 and new_score >= unique_ranked[i]:
#             i -= 1
#         current_ranking = i + 2  # Adding 2 to adjust for 0-based index and 1-based ranking
#         rankings.append(current_ranking)

#     return rankings

# ranked = [100, 100, 50, 40, 40, 20, 10]
# player = [5, 25, 50, 120]

# print(climbingLeaderboard(ranked, player))
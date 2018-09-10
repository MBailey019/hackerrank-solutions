#!/bin/python

import os
import math

def climbingLeaderboard(scores, alice):

    scores.append(0)
    scores_index = 0
    alice_index = len(alice)-1
    rank = 0
    ranks = []

    last_score = object()
    while alice_index >= 0:

        a_score = scores[scores_index]
        alice_score = alice[alice_index]

        if a_score != last_score:
            rank += 1
        if a_score <= alice_score:
            ranks.append(rank)
            alice_index -= 1
        else:
            scores_index += 1
        last_score = a_score

    return reversed(ranks)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    alice_count = int(raw_input())

    alice = map(int, raw_input().rstrip().split())

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

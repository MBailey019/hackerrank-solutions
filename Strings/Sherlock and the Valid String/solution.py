#!/bin/python

from collections import Counter
import os

def isValid(s):
    count_counts = Counter(Counter(s).values())
    most_common = count_counts.most_common(3)
    possible = 'YES'
    if len(most_common) != 1:

        if len(most_common) > 2:
            return 'NO'
        if most_common[1][1] == 1:
            if abs(most_common[0][0] - most_common[1][0]) > 1\
                    and most_common[1][0] != 1:
                possible = 'NO'
        else:
            possible = 'NO'
    return possible

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

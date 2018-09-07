#!/bin/python

import math
import os
import random
import re
import sys


def organizingContainers(container):
    num_of_types = []
    num_in_conts = []
    size = len(container)
    for i in range(size):
        of_type = 0
        in_cont = 0
        for j in range(size):
            of_type += container[i][j]
            in_cont += container[j][i]
        num_of_types.append(of_type)
        num_in_conts.append(in_cont)
    print(sorted(num_in_conts))
    print(sorted(num_of_types))
    if sorted(num_in_conts) == sorted(num_of_types):
        return 'Possible'
    else:
        return 'Impossible'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        n = int(raw_input())

        container = []

        for _ in xrange(n):
            container.append(map(int, raw_input().rstrip().split()))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

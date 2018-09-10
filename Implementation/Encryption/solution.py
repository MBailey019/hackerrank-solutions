#!/bin/python

from math import sqrt, ceil
import os

def encryption(s):
    c = int(ceil(sqrt(len(s))))
    enc = ''
    for r in range(c):
        i = r
        while i < len(s):
            enc += s[i]
            i += c
        enc += ' '

    return enc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

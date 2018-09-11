#!/bin/python

import os

def camelcase(s):
    count = 1
    for letter in s:
        count += letter.isupper()
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

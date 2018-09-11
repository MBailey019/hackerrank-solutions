#!/bin/python

import os
import re

def minimumNumber(n, password):
    missing_len = 6-len(password)

    lower = re.search('[a-z]',password)
    upper = re.search('[A-Z]',password)
    num = re.search('[0-9]',password)
    spec = re.search('[!@#$%^&*()--+]',password)

    missing_chars = (lower is None) + (upper is None) + (num is None) + (spec is None)

    return max(missing_len, missing_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

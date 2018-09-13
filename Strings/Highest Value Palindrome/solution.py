#!/bin/python

import os

# The tactic here is to break the moves into as many pairs as possible,
# since pairs can be used to place 9's at either end, which is always
# the optimal move. I then work out from the center, using single moves
# to copy digits one way or the other, breaking pairs into single as needed.
def highestValuePalindrome(s, n, k):
    s_L = list(s)
    pairs = k/2
    singles = k % 2
    m = (n/2)
    has_center = False
    if n == 1:
        front = []
        back = []
        has_center = True
        center = s_L
    else:
        front = s_L[0:m:1]
        back = s_L[-1:-(m+1):-1]
        center = []
        if n % 2 != 0:
            center = [s_L[m]]
            has_center = True

    comp = [int(back[i])-int(digit) for i,digit in enumerate(front)]
    nines_pairs = [] # don't have to do anything
    nines_singles = [] #leave for now
    others = [] #place nines
    i = 0
    for p in range(1, pairs+1):
        while True:
            if i >= m:
                singles += (pairs-p+1)*2
                i -= 1
                break
            if front[i] == '9' or back[i] == '9':
                if comp[i] == 0:
                    nines_pairs.append(i)
                    i += 1
                else:
                    nines_singles.append(i)
                    i += 1
            else:
                others.append(i)
                i += 1
                break

    to_fix = nines_singles + list(range(i,m))
    for position in to_fix[-1::-1]:
        if comp[position] != 0:
            if singles > 0:
                singles -= 1
            elif len(others) > 0 : # break up furthest-in pair of 9's
                removed = others.pop()
                if comp[removed] == 0:
                    singles += 1 # get 2 back from undoing 9's, use one for copy
                else:
                    singles += 0 # get 2 back from undoing 9's, use two for copies
                    if comp[removed] > 0:
                        front[removed] = back[removed]
            else:
                return '-1'
            if comp[position] > 0:
                front[position] = back[position]
    for position in others:
        front[position] = '9'
    if has_center and singles > 0:
        center[0] = '9'
    final = front + center + front[-1::-1]

    return ''.join(map(str,final))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = raw_input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()

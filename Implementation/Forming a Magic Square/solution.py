#!/bin/python

import os

def rotate_90ccw(m):
    return [[m[0][2],m[1][2],m[2][2]],
            [m[0][1],m[1][1],m[2][1]],
            [m[0][0],m[1][0],m[2][0]]]

def mirror_y(m):
    return[[m[0][2],m[0][1],m[0][0]],
           [m[1][2],m[1][1],m[1][0]],
           [m[2][2],m[2][1],m[2][0]]]

def formingMagicSquare(s):
    magic_sq = [[8,3,4],[1,5,9],[6,7,2]]

    costs = []
    for flip in range(2):
        for rot in range(4):
            cost = 0
            for i in range(3):
                for j in range(3):
                    c = abs(magic_sq[i][j]-s[i][j])
                    cost += c
            costs.append(cost)
            magic_sq = rotate_90ccw(magic_sq)
        magic_sq = mirror_y(magic_sq)

    return(min(costs))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

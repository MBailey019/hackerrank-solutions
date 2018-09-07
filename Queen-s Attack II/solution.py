#!/bin/python

import os

def queensAttack(n, k, r_q, c_q, obstacles):
    # Make each direction into a list of moves
    north = r_q-1
    east = n-c_q
    south = n-r_q
    west = c_q-1
    ne = min([r_q-1,n-c_q])
    se = min([n-r_q,n-c_q])
    sw = min([n-r_q,c_q-1])
    nw = min([c_q-1,r_q-1])
    
    # Place obstacles on appropriate list
    for obs in obstacles:
        qto = (obs[0]-r_q, obs[1]-c_q) #vector from queen to obstacle
        if abs(qto[0]) == abs(qto[1]):
            if qto[0] > 0:
                if qto[1] > 0:
                    se = min([qto[0]-1, se])
                else:
                    sw = min([qto[0]-1, sw])
            else:
                if qto[1] > 0:
                    ne = min([qto[1]-1, ne])
                else:
                    nw = min([abs(qto[0])-1, nw])
        elif qto[0] == 0:
            if qto[1] > 0:
                east = min([qto[1]-1, east])
            else:
                west = min([abs(qto[1])-1, west])
        elif qto[1] == 0:
            if qto[0] > 0:
                south = min([qto[0]-1, south])
            else:
                north = min([abs(qto[0])-1, north])   
        else:
            pass # Obstacle not on queen's path
        
    # Count up to nearest obstacle on each
    
    directions = [north, east, south, west, ne, se, sw, nw]
    print directions
    total_moves = sum(directions)
        
    return total_moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = raw_input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in xrange(k):
        obstacles.append(map(int, raw_input().rstrip().split()))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python

import os

def insertionSort1(n, arr):
    inserted = False
    current_index = n-1
    to_insert = arr[current_index] 
    while not inserted:
        if current_index == 0 or arr[current_index-1] < to_insert:
            arr[current_index] = to_insert
            inserted = True
        else:
            arr[current_index] = arr[current_index-1]
            current_index -= 1
        print ' '.join(map(str,arr))
        
if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    insertionSort1(n, arr)

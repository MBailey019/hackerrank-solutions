#!/bin/python

import os

def insertionSort1(arr, i):
    inserted = False
    current_index = i
    to_insert = arr[current_index] 
    while not inserted:
        if current_index == 0 or arr[current_index-1] < to_insert:
            arr[current_index] = to_insert
            inserted = True
        else:
            arr[current_index] = arr[current_index-1]
            current_index -= 1
    return arr
            
def insertionSort2(n, arr):
    sort_frame = 1 # index of 'sorting frame'
    while sort_frame < n:
        arr = insertionSort1(arr, sort_frame)
        print ' '.join(map(str,arr))
        sort_frame += 1
    
if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    insertionSort2(n, arr)

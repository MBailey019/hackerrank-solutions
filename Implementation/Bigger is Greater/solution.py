#!/bin/python

import os

def biggerIsGreater(w):
    print(w)
    word = [letter for letter in w]
    split_pt = None
    for i in reversed(range(len(w)-1)):
        if word[i] < word[i+1]:
            split_pt = i+1
            swap_a = word[i]
            print(swap_a)
            break
    if not split_pt:
        return 'no answer'
    
    print(word[:split_pt],sorted(word[split_pt:]))
    word = word[:split_pt] + sorted(word[split_pt:])
    swap_b = ''
    for index,letter in enumerate(word[split_pt:]):
        if letter > swap_a:
            swap_b = letter
            word[index+split_pt] = swap_a
            word[split_pt-1] = swap_b
            break
    return ''.join(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(raw_input())

    for T_itr in xrange(T):
        w = raw_input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

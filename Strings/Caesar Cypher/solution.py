#!/bin/python

import os

def move(character,n):
    if ord('A') <= ord(character) <= ord('Z')\
        or ord('a') <= ord(character) <= ord('z'):
        if character.isupper():
            start = ord('A')
            end = ord('Z')
        else:
            start = ord('a')
            end = ord('z')
        from_start = ord(character)-start+n
        new_int = from_start % (end-start+1)
        character = chr(new_int+start)
    return character

def caesarCipher(s, k):
    new_word = [move(letter, k) for letter in s]
    return ''.join(new_word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    k = int(raw_input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

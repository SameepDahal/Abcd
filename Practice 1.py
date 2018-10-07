#!/bin/python3

import sys

def alternatingCharacters(s):
    newstr=s[0]
    count=0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            count+=1
        else:
            newstr=newstr + s[i]
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)

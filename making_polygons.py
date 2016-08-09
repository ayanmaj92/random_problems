#!/bin/python3

import sys

#Here we need to use Euclidean formula to determine if a given set of segments can make a polygon or not.
#Check for each segment, and for each side that does NOT match, we simply need to do a cut there!
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
total = sum(a)
cuts = 0
for i in range(n):
    if a[i] >= total / 2:
        cuts = cuts + 1
print (cuts) 

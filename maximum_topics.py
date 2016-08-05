#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)
max_top = -1
max_team = 0
for i in range(n-1):
    for j in range(i+1,n):
        a = int(topic[i],2)
        b = int(topic[j],2)
        subs = bin(a | b).count('1')
        if subs > max_top:
            max_top = subs
            max_team = 1
        elif subs == max_top:
            max_team = max_team + 1
print (max_top)
print (max_team)

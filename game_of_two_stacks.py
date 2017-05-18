#!/bin/python3

import sys

#########################################
# Here, we first take as much as possible
# from the 1st stack. Then, we keep the 
# total number of tokens we have taken as 
# temp solution. Now, we start taking from
# the second stack. For each we take, we 
# remove elements that we have already taken
# from the 1st stack, in order to keep sum
# less than max. At these points, the count
# of the number of tokens remaining of i and
# j are added and checked with the temporary
# count. If we have more now, we set this as
# new temporary count.
###########################################

g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    # your code goes here
    i,j,total,count = 0,0,0,0
    while i < n and total + a[i] <= x:
        total += a[i]
        i += 1
    count = i
    while j < m and i >= 0:
        total += b[j]
        j += 1
        while total > x and i > 0:
            i -= 1
            total -= a[i]
        if total <= x and (i + j) > count:
            count = i + j
    print (count)

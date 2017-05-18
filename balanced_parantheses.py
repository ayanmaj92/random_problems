#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    stack = []
    flag = 0
    for b in s:
        if b in ['(','{','[']:
            stack.append(b)
        elif b in [')','}',']']:
            if len(stack) == 0:
                print ("NO")
                flag = 1
                break
            elif (stack[-1] == '(' and b != ')') or (stack[-1] == '{' and b != '}') or (stack[-1] == '[' and b != ']'):
                #print ("Right here")
                print ("NO")
                flag = 1
                break
            elif (stack[-1] == '(' and b == ')') or (stack[-1] == '{' and b == '}') or (stack[-1] == '[' and b == ']'):
                stack.pop()
    if flag == 0:
        if len(stack) != 0:
            print ("NO")
        else:
            print ("YES")
      

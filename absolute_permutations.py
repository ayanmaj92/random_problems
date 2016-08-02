#!/bin/python3

t = int(input().strip())
for i in range(t):
    flag = 0
    in1 = input().strip().split()
    n = int(in1[0])
    k = int(in1[1])
    l1 = []
    f = [0]*n
    #print ("Test:",i)
    #print (n,k)
    for num in range(1,n+1):
        a = num - k
        b = num + k
        if a <= 0 and b > n:
            print (-1)
            flag = 1
            break
        else:
            if a > 0 and f[a-1] != 1:
                l1.append(str(a))
                f[a-1] = 1
            elif b <= n:
                l1.append(str(b))
                f[b-1] = 1
            else:
                print (-1)
                flag = 1
                break
    if flag == 0:
        print (' '.join(l1))

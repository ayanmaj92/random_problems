#!/bin/python3
n, d = input().strip().split()
n, d = int(n), int(d)
share = input().strip().split()
for i in range(len(share)):
    share[i] = int(share[i])
for i in range(d):
    #print("Test:",i)
    prof = int(input().strip())
    days = 10**8
    min_t = None
    flag = 0
    dict_d = {}
    for j in range(len(share)):
        init = share[j]
        dict_d[init] = j
        if init-prof > 0 and init-prof in dict_d:
            if dict_d[init] - dict_d[init-prof] < days:
                days = dict_d[init] - dict_d[init-prof]
                flag = 1
                min_t = str(dict_d[init-prof]+1) + " " + str(dict_d[init]+1)
    if flag == 1:
        print (min_t)
    else:
        print (-1)

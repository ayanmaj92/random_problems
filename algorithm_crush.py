#uses python3

inp = input()
arr = [int (x) for x in inp.split()]
n,m = arr[0],arr[1]

list1 = [0 for _ in range(n)]

for _ in range(m):
    arr = input()
    arr = [int(x) for x in arr.split()]
    a,b,k = arr[0],arr[1],arr[2]
    list1[a-1] += k
    if b < n: 
        #print (b+1)
        #print (arr)
        list1[b] -= k
max,x = 0,0
#print (list1)
for i in range(n):
    x += list1[i]
    if max < x:
        max = x
        
print (max)

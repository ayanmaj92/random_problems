#!/bin/python3

b1 = input().strip().split()
n = int(b1[0])
m = int(b1[1])
adj = [[] for i in range(n)]

seen = [0 for i in range(n)]
weights = [0 for i in range(n)]
cuts = []
total_weight = 0
def dfs(node):
    seen[node] = 1
    for i in adj[node]:
        if not seen[i]:
            dfs(i)
    w = 0
    for i in adj[node]:
        w = w + weights[i]
    weights[node] = w + 1
    if weights[node] % 2 == 0:
        cuts.append(node+1)
        weights[node] = 0

for i in range(m):
    u,v = input().strip().split()
    u,v = int(u)-1, int(v)-1
    if not (v in adj[u]):
        adj[u].append(v)
    if not (u in adj[v]):
        adj[v].append(u)
dfs(0)
#print (weights)
#print (cuts)
print (len(cuts) - 1)
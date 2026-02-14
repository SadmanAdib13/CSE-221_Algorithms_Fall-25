from math import gcd
 
n, m = map(int, input().split())
 
adj = [[] for _ in range(n+1)]
 
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j and gcd(i, j) == 1:
            adj[i].append(j)
    adj[i].sort()
 
for _ in range(m):
    x, k = map(int, input().split())
    if k > len(adj[x]):
        print(-1)
    else:
        print(adj[x][k-1])
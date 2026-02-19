import sys
from collections import deque
inp = sys.stdin.readline
 
n, m, s, d, k = map(int, inp().split())
g = [[] for _ in range(n + 1)]
 
for _ in range(m):
    a, b = map(int, inp().split())
    g[a].append(b)
 
def bfs(st):
    q = deque([st])
    ds = [-1] * (n + 1)
    pr = [-1] * (n + 1)
    ds[st] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if ds[v] == -1:
                ds[v] = ds[u] + 1
                pr[v] = u
                q.append(v)
    return ds, pr
 
d1, p1 = bfs(s)
d2, p2 = bfs(k)
 
if d1[k] == -1 or d2[d] == -1:
    print(-1)
    exit()
 
pA = []
x = k
while x != -1:
    pA.append(x)
    x = p1[x]
pA.reverse()
 
pB = []
x = d
while x != -1:
    pB.append(x)
    x = p2[x]
pB.reverse()
 
p = pA + pB[1:]
 
print(len(p) - 1)
print(*p)
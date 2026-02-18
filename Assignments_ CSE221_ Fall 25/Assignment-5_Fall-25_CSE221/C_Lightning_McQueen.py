import sys
from collections import deque
input = sys.stdin.readline
 
N, M, S, D = map(int, input().split())
 
if M > 0:
    U = list(map(int, input().split()))
    V = list(map(int, input().split()))
else:
    U = []
    V = []
 
G = [[] for _ in range(N + 1)]
for i in range(M):
    a = U[i]
    b = V[i]
    G[a].append(b)
    G[b].append(a)
 
for i in range(1, N + 1):
    G[i].sort()
 
if S == D:
    print(0)
    print(S)
    sys.exit()
 
dist = [-1] * (N + 1)
par = [-1] * (N + 1)
 
q = deque([S])
dist[S] = 0
 
while q:
    u = q.popleft()
    if u == D:
        break
    for v in G[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            par[v] = u
            q.append(v)
 
if dist[D] == -1:
    print(-1)
    sys.exit()
 
path = []
x = D
while x != -1:
    path.append(x)
    x = par[x]
 
path.reverse()
 
print(dist[D])
print(*path)
from collections import deque
import sys
 
input = sys.stdin.readline
 
def BFS(G, s):
    n = len(G) - 1
    colour = [0] * (n + 1)
 
    Q = deque()
    colour[s] = 1
    Q.append(s)
 
    order = []
 
    while Q:
        u = Q.popleft()
        order.append(u)
 
        for v in G[u]:
            if colour[v] == 0:
                colour[v] = 1
                Q.append(v)
 
    return order
 
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
 
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
 
for u in range(1, N + 1):
    G[u].sort()
 
ans = BFS(G, 1)
print(*ans)
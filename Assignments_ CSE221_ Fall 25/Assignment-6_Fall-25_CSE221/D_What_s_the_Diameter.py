import sys
from collections import deque
input = sys.stdin.readline
 
def bfs(start, n, g):
    dist = [-1]*(n+1)
    dist[start] = 0
    q = deque([start])
    far_node = start
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[far_node]:
                    far_node = v
    return far_node, dist
 
def run():
    n = int(input())
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
 
    u, _ = bfs(1, n, g)
    v, dist = bfs(u, n, g)
    diameter = dist[v]
    print(diameter)
    print(u, v)
 
run()
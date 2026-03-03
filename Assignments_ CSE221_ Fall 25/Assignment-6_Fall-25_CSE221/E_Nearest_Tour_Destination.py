import sys
from collections import deque
 
input = sys.stdin.readline
 
 
def run():
    n, m, s, q = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
 
    src = list(map(int, input().split()))
    dst = list(map(int, input().split()))
 
    dist = [-1] * (n + 1)
    qd = deque()
    for x in src:
        dist[x] = 0
        qd.append(x)
 
    while qd:
        u = qd.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                qd.append(v)
 
    res = [str(dist[x]) for x in dst]
    print(" ".join(res))
 
 
run()
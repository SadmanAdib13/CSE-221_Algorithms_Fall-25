import sys
from collections import deque
input = sys.stdin.readline
 
def run():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
 
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
 
    col = [-1] * (n + 1)
    ans = 0
 
    for s in range(1, n + 1):
        if col[s] == -1:
            q = deque([s])
            col[s] = 0
            c0 = 1
            c1 = 0
 
            while q:
                u = q.popleft()
                for v in g[u]:
                    if col[v] == -1:
                        col[v] = col[u] ^ 1
                        if col[v] == 0:
                            c0 += 1
                        else:
                            c1 += 1
                        q.append(v)
 
            ans += max(c0, c1)
 
    print(ans)
 
run()
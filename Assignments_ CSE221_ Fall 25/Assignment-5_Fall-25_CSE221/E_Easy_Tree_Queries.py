import sys
sys.setrecursionlimit(300000)
inp = sys.stdin.readline
 
n, r = map(int, inp().split())
g = [[] for _ in range(n+1)]
 
for _ in range(n-1):
    u, v = map(int, inp().split())
    g[u].append(v)
    g[v].append(u)
 
sz = [0] * (n+1)
 
def dfs(x, p):
    sz[x] = 1
    for y in g[x]:
        if y != p:
            dfs(y, x)
            sz[x] += sz[y]
 
dfs(r, 0)
 
q = int(inp())
out = []
for _ in range(q):
    x = int(inp())
    out.append(str(sz[x]))
 
print("\n".join(out))
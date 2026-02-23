import sys
sys.setrecursionlimit(300000)
inp = sys.stdin.readline
 
n, m = map(int, inp().split())
g = [[] for _ in range(n+1)]
 
for _ in range(m):
    u, v = map(int, inp().split())
    g[u].append(v)
 
 
col = [0]*(n+1)
has_cycle = False
 
def dfs(x):
    global has_cycle
    col[x] = 1
    for y in g[x]:
        if col[y] == 0:
            dfs(y)
            if has_cycle:
                return
        elif col[y] == 1:
            has_cycle = True
            return
    col[x] = 2
 
for i in range(1, n+1):
    if col[i] == 0:
        dfs(i)
        if has_cycle:
            break
 
print("YES" if has_cycle else "NO")
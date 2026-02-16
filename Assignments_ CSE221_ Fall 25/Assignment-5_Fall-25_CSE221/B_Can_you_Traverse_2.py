import sys
sys.setrecursionlimit(2*100000 + 5)
input = sys.stdin.readline
 
def colourInitializing(G):
    return [0] * (len(G))
 
def DFS(G, u, colour, ans):
    colour[u] = 1
    ans.append(u)
    for v in G[u]:
        if colour[v] == 0:
            DFS(G, v, colour, ans)
 
 
# ----------- MAIN -------------
N, M = map(int, input().split())
u_line = list(map(int, input().split()))
v_line = list(map(int, input().split()))
 
G = [[] for _ in range(N + 1)]
 
for i in range(M):
    u = u_line[i]
    v = v_line[i]
    G[u].append(v)
    G[v].append(u)
 
for u in range(1, N + 1):
    G[u].sort()
 
colour = colourInitializing(G)
ans = []
 
DFS(G, 1, colour, ans)
 
print(*ans)
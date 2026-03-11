import heapq
 
INF = 10**18
 
def dijk(st, g, n):
    d = [INF] * (n + 1)
    d[st] = 0
    pq = [(0, st)]
    while pq:
        cd, u = heapq.heappop(pq)
        if cd > d[u]:
            continue
        for v, w in g[u]:
            nd = cd + w
            if nd < d[v]:
                d[v] = nd
                heapq.heappush(pq, (nd, v))
    return d
 
def solve():
    n, m, s, t = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
 
    da = dijk(s, g, n)
    db = dijk(t, g, n)
 
    bt = INF
    mn = -1
 
    for i in range(1, n + 1):
        if da[i] < INF and db[i] < INF:
            mt = max(da[i], db[i])
            if mt < bt or (mt == bt and i < mn):
                bt = mt
                mn = i
 
    if mn == -1:
        print(-1)
    else:
        print(bt, mn)
 
solve()
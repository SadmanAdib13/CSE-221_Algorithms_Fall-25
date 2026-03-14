import heapq
 
INF = 10 ** 18
 
 
def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
 
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
 
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
 
    while pq:
        cd, u = heapq.heappop(pq)
        if cd > dist[u]:
            continue
        for v, w in g[u]:
            nd = max(cd, w)
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
 
    for i in range(1, n + 1):
        print(dist[i] if dist[i] != INF else -1, end=" ")
 
 
solve()
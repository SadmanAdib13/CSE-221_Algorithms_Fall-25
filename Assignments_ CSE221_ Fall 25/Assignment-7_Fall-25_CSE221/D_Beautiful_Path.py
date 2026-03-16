import heapq
 
INF = 10 ** 18
 
 
def solve():
    n, m, s, d = map(int, input().split())
    w = [0] + list(map(int, input().split()))
 
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
 
    dist = [INF] * (n + 1)
    dist[s] = w[s]
 
    pq = [(w[s], s)]
    while pq:
        cd, u = heapq.heappop(pq)
        if cd > dist[u]:
            continue
        for v in g[u]:
            nd = cd + w[v]
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
 
    print(dist[d] if dist[d] != INF else -1)
 
 
solve()
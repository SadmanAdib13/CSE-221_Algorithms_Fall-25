import heapq
 
 
def shortest_path():
    n, m, src, dst = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))
 
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u[i]].append((v[i], w[i]))
 
    INF = 10 ** 18
    dist = [INF] * (n + 1)
    par = [-1] * (n + 1)
 
    dist[src] = 0
    pq = [(0, src)]
 
    while pq:
        cd, x = heapq.heappop(pq)
        if cd > dist[x]:
            continue
        for y, wt in adj[x]:
            nd = cd + wt
            if nd < dist[y]:
                dist[y] = nd
                par[y] = x
                heapq.heappush(pq, (nd, y))
 
    if dist[dst] == INF:
        print(-1)
        return
 
    print(dist[dst])
    path = []
    while dst != -1:
        path.append(dst)
        dst = par[dst]
    print(*path[::-1])
 
 
shortest_path()
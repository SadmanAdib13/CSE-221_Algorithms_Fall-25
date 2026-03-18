import sys
import heapq
 
input = sys.stdin.readline
 
n, m, s, t = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
 
INF = int(1e18)
dist = [[INF, INF] for _ in range(n + 1)]
dist[s][0] = 0
 
pq = []
heapq.heappush(pq, (0, s))
 
while pq:
    d, u = heapq.heappop(pq)
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v][0]:
            dist[v][1] = dist[v][0]
            dist[v][0] = nd
            heapq.heappush(pq, (dist[v][0], v))
        elif dist[v][0] < nd < dist[v][1]:
            dist[v][1] = nd
            heapq.heappush(pq, (dist[v][1], v))
 
res = dist[t][1]
print(res if res != INF else -1)
import sys
import heapq
 
input = sys.stdin.readline
 
n, m = map(int, input().split())
uu = list(map(int, input().split()))
vv = list(map(int, input().split()))
ww = list(map(int, input().split()))
 
adj = [[] for _ in range(n + 1)]
for i in range(m):
    adj[uu[i]].append((vv[i], ww[i]))
 
INF = int(1e18)
dist = [[INF, INF] for _ in range(n + 1)]
 
pq = []
heapq.heappush(pq, (0, 1, -1))
 
while pq:
    d, nd, lp = heapq.heappop(pq)
    if lp != -1 and d > dist[nd][lp]:
        continue
    for nb, w in adj[nd]:
        ep = w % 2
        if lp == -1 or ep != lp:
            if dist[nb][ep] > d + w:
                dist[nb][ep] = d + w
                heapq.heappush(pq, (dist[nb][ep], nb, ep))
 
res = min(dist[n][0], dist[n][1])
print(res if res != INF else -1)
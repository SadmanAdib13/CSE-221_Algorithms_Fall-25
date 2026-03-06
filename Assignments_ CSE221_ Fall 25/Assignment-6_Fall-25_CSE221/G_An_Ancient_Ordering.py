import sys
import heapq
input = sys.stdin.readline
 
def run():
    n = int(input())
    w = [input().strip() for _ in range(n)]
    g = {c:set() for word in w for c in word}
    indeg = {c:0 for c in g}
 
    for i in range(n-1):
        a, b = w[i], w[i+1]
        minlen = min(len(a), len(b))
        diff_found = False
        for j in range(minlen):
            if a[j] != b[j]:
                if b[j] not in g[a[j]]:
                    g[a[j]].add(b[j])
                    indeg[b[j]] += 1
                diff_found = True
                break
        if not diff_found and len(a) > len(b):
            print(-1)
            return
 
    pq = []
    for c in g:
        if indeg[c]==0:
            heapq.heappush(pq, c)
    res = []
    while pq:
        u = heapq.heappop(pq)
        res.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                heapq.heappush(pq, v)
    if len(res) != len(g):
        print(-1)
        return
    print("".join(res))
 
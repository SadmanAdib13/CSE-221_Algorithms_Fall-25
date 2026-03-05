import sys
from collections import deque
input = sys.stdin.readline
 
MAX_T = 5000
 

factors = [set() for _ in range(MAX_T+1)]
is_prime = [True]*(MAX_T+1)
is_prime[0] = is_prime[1] = False
 
for i in range(2, MAX_T+1):
    if is_prime[i]:
        for j in range(i*2, MAX_T+1, i):
            is_prime[j] = False
            if j != i:
                factors[j].add(i)
 
def run():
    T = int(input())
    for _ in range(T):
        s, t = map(int, input().split())
        vis = [False]*(t+101)
        q = deque()
        q.append((s,0))
        vis[s] = True
        ans = -1
        while q:
            x, d = q.popleft()
            if x == t:
                ans = d
                break
            if x > t:
                continue
            for p in factors[x]:
                nx = x + p
                if nx <= t and not vis[nx]:
                    vis[nx] = True
                    q.append((nx, d+1))
        print(ans)
 
run()
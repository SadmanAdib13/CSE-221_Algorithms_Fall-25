import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
 
def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]
 
n, m = map(int, input().split())
e = []
 
for _ in range(m):
    u, v, w = map(int, input().split())
    e.append((w, u, v))
 
e.sort()
p = [i for i in range(n + 1)]
 
ans = 0
cnt = 0
 
for w, u, v in e:
    x = f(u)
    y = f(v)
    if x != y:
        p[y] = x
        ans += w
        cnt += 1
        if cnt == n - 1:
            break
 
print(ans)
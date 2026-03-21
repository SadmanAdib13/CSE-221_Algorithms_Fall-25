import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
 
def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]
 
n, k = map(int, input().split())
 
p = [i for i in range(n + 1)]
s = [1] * (n + 1)
 
for _ in range(k):
    a, b = map(int, input().split())
    x = f(a)
    y = f(b)
 
    if x != y:
        if s[x] < s[y]:
            x, y = y, x
        p[y] = x
        s[x] += s[y]
 
    print(s[f(a)])
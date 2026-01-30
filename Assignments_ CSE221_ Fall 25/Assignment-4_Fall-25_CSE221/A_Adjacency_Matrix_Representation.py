n, m = map(int, input().split())
g = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a-1][b-1] = c
for r in g:
    print(*r)
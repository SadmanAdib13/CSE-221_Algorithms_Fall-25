n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
 
g = [[] for _ in range(n)]
 
for i in range(m):
    g[u[i]-1].append((v[i], w[i]))
 
for i in range(n):
    print(i+1, end=": ")
    for x, y in g[i]:
        print(f"({x},{y})", end=" ")
    print()
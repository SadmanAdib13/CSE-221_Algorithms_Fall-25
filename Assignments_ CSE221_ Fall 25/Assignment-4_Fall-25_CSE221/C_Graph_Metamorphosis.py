n = int(input())
g = [[0]*n for _ in range(n)]
 
for i in range(n):
    lst = list(map(int, input().split()))
    k = lst[0]
    for j in range(1, k+1):
        g[i][lst[j]] = 1
 
for r in g:
    print(*r)
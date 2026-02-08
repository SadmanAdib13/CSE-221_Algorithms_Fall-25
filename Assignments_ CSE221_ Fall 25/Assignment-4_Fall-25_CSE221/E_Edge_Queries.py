n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
 
inn = [0]*n
out = [0]*n
 
for i in range(m):
    a = u[i]-1
    b = v[i]-1
    out[a] += 1
    inn[b] += 1
 
for i in range(n):
    print(inn[i] - out[i], end=" ")
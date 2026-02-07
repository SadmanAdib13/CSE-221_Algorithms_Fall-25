n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
 
deg = [0]*n
for i in range(m):
    a = u[i]-1
    b = v[i]-1
    deg[a] += 1
    deg[b] += 1
 
odd = 0
for x in deg:
    if x % 2 == 1:
        odd += 1
 
if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")
 
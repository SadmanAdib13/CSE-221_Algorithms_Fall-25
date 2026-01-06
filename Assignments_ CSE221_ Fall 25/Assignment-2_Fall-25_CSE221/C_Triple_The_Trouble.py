n, x = map(int, input().split())
a = list(map(int, input().split()))
 
found = False
for i in range(n):
    
    seen = {}
    target = x - a[i]
    for j in range(i + 1, n):
        if target - a[j] in seen:
            print(i + 1, seen[target - a[j]] + 1, j + 1)
            found = True
            break
        seen[a[j]] = j
    if found:
        break
 
if not found:
    print(-1)
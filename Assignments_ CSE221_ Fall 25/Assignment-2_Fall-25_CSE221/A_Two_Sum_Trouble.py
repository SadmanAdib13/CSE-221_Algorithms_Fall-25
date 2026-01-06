num, sum = map(int, input().split())
a = list(map(int, input().split()))
 
 
l = 0
r = num - 1
found = False
 
while l < r:
    current = a[l] + a[r]
    if current == sum:
        print(l + 1, r + 1)  # 1-based indices
        found = True
        break
    elif current < sum:
        l += 1
    else:
        r -= 1
 
if not found:
    print(-1)
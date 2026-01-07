 
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
 
l = 0
sum = 0
max_len = 0
 
for i in range(n):
    sum += a[i]
    
    
    while sum > k and l <= i:
        sum -= a[l]
        l += 1
 
    
    if sum <= k:
        max_len = max(max_len, i - l + 1)
 
print(max_len)
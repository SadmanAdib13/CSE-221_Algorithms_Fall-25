n, k = map(int, input().split())
a = list(map(int, input().split()))
 
c = {}
l = 0
a_len = 0
 
for i in range(n):
    c[a[i]] = c.get(a[i], 0) + 1
    while len(c) > k:
        c[a[l]] -= 1
        if c[a[l]] == 0:
            del c[a[l]]
        l += 1
    a_len = max(a_len, i - l + 1)
 
print(a_len)
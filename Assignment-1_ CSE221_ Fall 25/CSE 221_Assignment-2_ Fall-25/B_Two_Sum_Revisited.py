n, m, given = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
i = 0
j = m - 1
i1, j2 = 0, 0
min_diff = float('inf')
 
while i < n and j >= 0:
    sum = a[i] + b[j]
    diff = abs(sum - given)
    
    if diff < min_diff:
        min_diff = diff
        i1, j2 = i, j
    
    if sum > given:
        j -= 1
    else:
        i += 1
 
print(i1 + 1, j2 + 1)

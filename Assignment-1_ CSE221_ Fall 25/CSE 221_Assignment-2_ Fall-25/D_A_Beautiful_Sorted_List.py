n = int(input())
x = list(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))
 
i = 0
j = 0
mer = []
 
while i < n and j < m:
    if x[i] <= y[j]:
        mer.append(x[i])
        i += 1
    else:
        mer.append(y[j])
        j += 1
 
while i < n:
    mer.append(x[i])
    i += 1
 
while j < m:
    mer.append(y[j])
    j += 1
 
print(*mer)
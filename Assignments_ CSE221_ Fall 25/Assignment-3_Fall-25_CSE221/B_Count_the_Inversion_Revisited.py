from bisect import bisect_left, insort
 
n = int(input())
A = list(map(int, input().split()))
 
squared_list = []
count = 0
 
for i in range(n-1, -1, -1):
    pos = bisect_left(squared_list, A[i])
    count += pos
    insort(squared_list, A[i] ** 2)
 
print(count)
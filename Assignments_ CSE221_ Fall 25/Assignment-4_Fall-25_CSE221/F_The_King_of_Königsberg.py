s = int(input())
p, q = map(int, input().split())
 
d = [(-1,0),(1,0),(0,-1),(0,1),
     (-1,-1),(-1,1),(1,-1),(1,1)]
 
ans = []
for a, b in d:
    r = p + a
    c = q + b
    if 1 <= r <= s and 1 <= c <= s:
        ans.append((r, c))
 
ans.sort()
 
print(len(ans))
for r, c in ans:
    print(r, c)
h, w, t = map(int, input().split())
 
s = set()
for _ in range(t):
    u, v = map(int, input().split())
    s.add((u, v))
 
d = [(2,1),(2,-1),(-2,1),(-2,-1),
     (1,2),(1,-2),(-1,2),(-1,-2)]
 
for u, v in s:
    for a, b in d:
        x = u + a
        y = v + b
        if (x, y) in s:
            print("YES")
            exit()
 
print("NO")
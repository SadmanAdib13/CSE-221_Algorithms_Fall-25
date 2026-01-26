import sys
input = sys.stdin.readline
 
def post(i, p):
    if not i:
        return []
    r = p[0]
    idx = i.index(r)
    l = post(i[:idx], p[1:idx+1])
    ri = post(i[idx+1:], p[idx+1:])
    return l + ri + [r]
 
n = int(input())
i = list(map(int, input().split()))
p = list(map(int, input().split()))
r = post(i, p)
print(*r)

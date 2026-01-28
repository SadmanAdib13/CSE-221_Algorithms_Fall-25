import sys
input = sys.stdin.readline
 
def pre(i, po):
    if not i:
        return []
    r = po[-1]
    idx = i.index(r)
    l = pre(i[:idx], po[:idx])
    ri = pre(i[idx+1:], po[idx: -1])
    return [r] + l + ri
 
n = int(input())
i = list(map(int, input().split()))
po = list(map(int, input().split()))
r = pre(i, po)
print(*r)
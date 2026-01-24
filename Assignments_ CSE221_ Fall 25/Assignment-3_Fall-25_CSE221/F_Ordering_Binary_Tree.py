import sys
input = sys.stdin.readline

def bst(a):
    if not a:
        return []
    m = len(a) // 2
    return [a[m]] + bst(a[:m]) + bst(a[m+1:])

n = int(input())
A = list(map(int, input().split()))
r = bst(A)
print(*r)

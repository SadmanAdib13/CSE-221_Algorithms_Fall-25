def l_b(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l
 
def u_b(a, y):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] <= y:
            l = m + 1
        else:
            r = m
    return l
 
n, q = map(int, input().split())
a = list(map(int, input().split()))
 
for _ in range(q):
    x, y = map(int, input().split())
    left_index = l_b(a, x)
    right_index = u_b(a, y)
    print(right_index - left_index)
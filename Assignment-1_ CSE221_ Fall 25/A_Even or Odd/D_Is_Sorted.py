t = int(input())
while t > 0:
    n = int(input())
    arr = []
    while len(arr) < n:
        l = input().strip()
        if l == "":
            continue
        p = l.split()
        for x in p:
            arr.append(int(x))
            if len(arr) == n:
                break
    i = 0
    f = True
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            f = False
            break
        i += 1
    if f:
        print("YES")
    else:
        print("NO")
    t -= 1
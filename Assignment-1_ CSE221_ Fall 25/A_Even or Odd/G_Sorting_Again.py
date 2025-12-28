def read_ints(n):
    nums = []
    while len(nums) < n:
        line = input().strip()
        if not line:
            continue
        for x in line.split():
            nums.append(int(x))
            if len(nums) == n:
                break
    return nums
 
t = int(input())
res = []
 
for _ in range(t):
    n = int(input())
    ids = read_ints(n)
    mks = read_ints(n)
    sw = 0
 
    for i in range(n - 1):
        mx = i
        for j in range(i + 1, n):
            if mks[j] > mks[mx]:
                mx = j
            elif mks[j] == mks[mx] and ids[j] < ids[mx]:
                mx = j
        if mx != i:
            ids[i], ids[mx] = ids[mx], ids[i]
            mks[i], mks[mx] = mks[mx], mks[i]
            sw += 1
 
    out = [f"Minimum swaps: {sw}"]
    for k in range(n):
        out.append(f"ID: {ids[k]} Mark: {mks[k]}")
    res.append("\n".join(out))
 
print("\n".join(res))
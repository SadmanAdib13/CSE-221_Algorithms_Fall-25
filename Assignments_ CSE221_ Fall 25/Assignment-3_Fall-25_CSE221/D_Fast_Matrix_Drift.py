import sys
input = sys.stdin.readline
 
def matmult(a, b, m):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % m, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % m],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % m, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % m]
    ]
 
def matpower(a, n, m):
    r = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            r = matmult(r, a, m)
        a = matmult(a, a, m)
        n >>= 1
    return r
 
t = int(input())
m = 10**9 + 7
out = []
 
for _ in range(t):
    a11, a12, a21, a22 = map(int, input().split())
    x = int(input())
    A = [[a11, a12], [a21, a22]]
    r = matpower(A, x, m)
    out.append(f"{r[0][0]} {r[0][1]}\n{r[1][0]} {r[1][1]}")
 
sys.stdout.write("\n".join(out))
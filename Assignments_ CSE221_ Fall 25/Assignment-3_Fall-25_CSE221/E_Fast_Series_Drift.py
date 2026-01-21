import sys
input = sys.stdin.readline
 
def fast_series(a, n, m):
    
    res_sum = 0
    res_pow = 1
    cur_sum = a % m
    cur_pow = a % m
    while n > 0:
        if n & 1:
            res_sum = (res_sum * cur_pow + cur_sum) % m
            res_pow = (res_pow * cur_pow) % m
        cur_sum = (cur_sum * (1 + cur_pow)) % m
        cur_pow = (cur_pow * cur_pow) % m
        n >>= 1
    return res_sum % m
 
T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(fast_series(a, n, m))

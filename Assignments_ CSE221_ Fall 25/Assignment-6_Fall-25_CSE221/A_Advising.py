import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
 
def run():
    n, m = map(int, input().split())
 
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
 
    st = [0] * (n + 1)   # 0=unvisited, 1=visiting, 2=done
    res = []             # topo order
    bad = [False]        # cycle flag
 
    def dfs(x):
        if bad[0]:
            return
        st[x] = 1
 
        for y in g[x]:
            if st[y] == 0:
                dfs(y)
            elif st[y] == 1:
                bad[0] = True
                return
 
        st[x] = 2
        res.append(x)
 
    for i in range(1, n + 1):
        if st[i] == 0:
            dfs(i)
 
    if bad[0]:
        print(-1)
    else:
        res.reverse()
        print(*res)
 
 
if __name__ == "__main__":
    run()
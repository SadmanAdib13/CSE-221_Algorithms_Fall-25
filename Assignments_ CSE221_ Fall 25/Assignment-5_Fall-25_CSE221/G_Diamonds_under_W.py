import sys
from collections import deque
sys.setrecursionlimit(3000000)
inp = sys.stdin.readline
 
R, C = map(int, inp().split())
g = [list(inp().strip()) for _ in range(R)]
 
vis = [[0]*C for _ in range(R)]
ans = 0
 
for i in range(R):
    for j in range(C):
        if g[i][j] != '#' and not vis[i][j]:
            q = deque([(i, j)])
            vis[i][j] = 1
            cnt = 0
            while q:
                x, y = q.popleft()
                if g[x][y] == 'D':
                    cnt += 1
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if g[nx][ny] != '#' and not vis[nx][ny]:
                            vis[nx][ny] = 1
                            q.append((nx, ny))
            ans = max(ans, cnt)
 
print(ans)
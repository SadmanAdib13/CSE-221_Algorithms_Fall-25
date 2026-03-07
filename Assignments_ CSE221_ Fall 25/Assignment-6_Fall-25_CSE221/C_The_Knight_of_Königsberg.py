from collections import deque
 
def knight():
    n = int(input().strip())
    x1, y1, x2, y2 = map(int, input().split())
 
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
 
    if x1 == x2 and y1 == y2:
        print(0)
        return
 
    mv = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
 
    vis = [[False] * n for _ in range(n)]
    q = deque()
 
    q.append((x1, y1, 0))
    vis[x1][y1] = True
 
    while q:
        x, y, d = q.popleft()
 
        for dx, dy in mv:
            nx = x + dx
            ny = y + dy
 
            if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                if nx == x2 and ny == y2:
                    print(d + 1)
                    return
 
                vis[nx][ny] = True
                q.append((nx, ny, d + 1))
 
    print(-1)
 
 
knight()
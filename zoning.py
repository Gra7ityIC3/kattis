from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

n = int(input())
grid, q = [], deque()
dist = [[-1] * n for _ in range(n)]
for r in range(n):
    grid.append(input())
    for c in range(n):
        if grid[r][c] == '3':
            dist[r][c] = 0
            q.append((r, c))
while q:
    r, c = q.popleft()
    if grid[r][c] == '1':
        ans = dist[r][c]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
print(ans)
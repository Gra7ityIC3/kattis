from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)

n, m = map(int, input().split())
grid = [[*map(int, input())] for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])
while q and dist[-1][-1] == -1:
    r, c = q.popleft()
    for d in range(4):
        nr = r + dr[d] * grid[r][c]
        nc = c + dc[d] * grid[r][c]
        if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
print(dist[-1][-1])
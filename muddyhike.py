from heapq import *

dr = (-1, 1, 0, 0)
dc = (0, 0, 1, -1)

n, m = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
pq = [(grid[r][0], r, 0) for r in range(n)]
heapify(pq)
ans = 0
while True:
    d, r, c = heappop(pq)
    ans = max(ans, d)
    if c == m - 1:
        print(ans)
        break
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != -1:
            heappush(pq, (grid[nr][nc], nr, nc))
    grid[r][c] = - 1
from heapq import heappush, heappop

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

h, w = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(h)]
i, j = map(int, input().split())
i, j = i - 1, j - 1
dist = [[0] * w for _ in range(h)]
dist[i][j] = grid[i][j]
pq = [(grid[i][j], i, j)]
while pq:
    d, r, c = heappop(pq)
    if d == dist[r][c]:
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < h and 0 <= nc < w and max(d, grid[nr][nc]) < dist[nr][nc]:
                dist[nr][nc] = max(d, grid[nr][nc])
                heappush(pq, (dist[nr][nc], nr, nc))
print(sum(-dist[r][c] for r in range(h) for c in range(w)))
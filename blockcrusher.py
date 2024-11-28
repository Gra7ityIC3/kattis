from heapq import *

INF = 10 ** 9

dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

while True:
    h, w = map(int, input().split())
    if h == 0: break
    grid = [[*map(int, input())] for _ in range(h)]
    dist = [[INF] * w for _ in range(h)]
    p = [[0] * w for _ in range(h)]
    pq = []
    for c in range(w):
        dist[0][c] = grid[0][c]
        pq.append((dist[0][c], 0, c))
    heapify(pq)
    while True:
        d, r, c = heappop(pq)
        if r == h - 1: break
        if d == dist[r][c]:
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < h and 0 <= nc < w and d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    p[nr][nc] = (r, c)
                    heappush(pq, (dist[nr][nc], nr, nc))
    while p[r][c]:
        grid[r][c] = ' '
        r, c = p[r][c]
    grid[r][c] = ' '
    for row in grid: print(*row, sep='')
    print()
from heapq import heappush, heappop

dr = (0, 0, -1, 1)
dc = (-1, 1, 0, 0)

n = int(input())
grid = [[*map(int, input().split())] for _ in range(n)]
pq = [(0, 0, 0)]
ans = 0
while True:
    d, r, c = heappop(pq)
    ans = max(ans, d)
    if r == n - 1 and c == n - 1:
        print(ans)
        break
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
            heappush(pq, (grid[nr][nc], nr, nc))
    grid[r][c] = -1
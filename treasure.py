from collections import deque

INF = 10 ** 9

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
cost = {'S': 1, 'G': 1, '.': 1, 'F': 2, 'M': 3}

n, m, k = map(int, input().split())
grid, q = [], deque()
dist = [[[INF] * (k + 1) for _ in range(m)] for _ in range(n)]
for r in range(n):
    grid.append(input())
    for c in range(m):
        if grid[r][c] == 'S':
            dist[r][c][k] = 1
            q.append((1, r, c, k))
while q:
    d, r, c, x = q.popleft()
    if grid[r][c] == 'G':
        print(d)
        break
    if d == dist[r][c][x]:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                y = cost[grid[nr][nc]]
                if x >= y and d < dist[nr][nc][x - y]:
                    dist[nr][nc][x - y] = d
                    q.appendleft((d, nr, nc, x - y))
        if d + 1 < dist[r][c][k]:
            dist[r][c][k] = d + 1
            q.append((d + 1, r, c, k))
else:
    print(-1)
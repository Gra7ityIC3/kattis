from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

t, n, m = map(int, input().split())
grid, q = [], deque()
for r in range(n):
    grid.append([*input()])
    for c in range(m):
        if grid[r][c] == 'S':
            q.append((0, r, c))
while q:
    d, r, c = q.popleft()
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            print('NOT POSSIBLE' if d > t else d)
            exit()
        if grid[nr][nc] == '0' or grid[nr][nc] == ('D', 'U', 'R', 'L')[k]:
            grid[nr][nc] = 'S'
            q.append((d + 1, nr, nc))
print('NOT POSSIBLE')
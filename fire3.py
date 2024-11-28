from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

R, C = map(int, input().split())
grid, q = [], deque()
for r in range(R):
    grid.append([*input()])
    for c in range(C):
        if grid[r][c] in 'JF':
            q.append((1, r, c))
while q:
    d, r, c = q.popleft()
    if grid[r][c] == 'J':
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                print(d)
                exit()
            if grid[nr][nc] == '.':
                grid[nr][nc] = 'J'
                q.append((d + 1, nr, nc))
    else:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] in '.J':
                grid[nr][nc] = 'F'
                q.append((d + 1, nr, nc))
print('IMPOSSIBLE')
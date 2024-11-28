dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def floodfill(r, c):
    grid[r][c] = 'W'
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 'W':
            floodfill(nr, nc)

R, C = map(int, input().split())
grid = [[*input()] for _ in range(R)]
ans = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'L':
            ans += 1
            floodfill(r, c)
print(ans)
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

def floodfill(r, c):
    grid[r][c] = '.'
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '#':
            floodfill(nr, nc)

R, C = map(int, input().split())
grid = [[*input()] for _ in range(R)]
ans = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '#':
            ans += 1
            floodfill(r, c)
print(ans)
dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)

R, C = map(int, input().split())
grid = [[*input()] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if grid[r][c] == '.':
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'E':
                    break
            else:
                grid[r][c] = 'E'
for row in grid:
    print(''.join(row))
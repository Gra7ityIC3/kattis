r, c = map(int, input().split())
grid = [input() for _ in range(r)]
print(''.join(grid[i][j] for j in range(c) for i in range(r) if grid[i][j] != '.'))
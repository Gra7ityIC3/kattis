R, C = map(int, input().split())
grid = [[*input()] for _ in range(R)]
for c in range(C):
    offset = 0
    for r in range(R - 1, -1, -1):
        if grid[r][c] == 'a':
            grid[r][c] = '.'
            grid[r + offset][c] = 'a'
        elif grid[r][c] == '.':
            offset += 1
        else:
            offset = 0
for row in grid:
    print(''.join(row))
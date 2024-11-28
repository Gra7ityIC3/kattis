import sys
sys.setrecursionlimit(250000)

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def floodfill(r, c):
    grid[r][c] = 'S'
    ans = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '#':
            ans += floodfill(nr, nc)
    return ans

R = int(input())
C = int(input())
U = int(input())
grid = [[*input()] for _ in range(R)]
ans = next(floodfill(r, c) for r in range(R) for c in range(C) if grid[r][c] == 'S')
print(ans)
for _ in range(U):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'S':
            ans += floodfill(r, c)
            break
    else:
        grid[r][c] = '#'
    print(ans)
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

def neighbors(r, c):
    ans = 0
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        ans += 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 'o'
    return ans

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
total = mirko = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'o':
            total += neighbors(r, c)
        else:
            mirko = max(mirko, neighbors(r, c))
print(total // 2 + mirko)
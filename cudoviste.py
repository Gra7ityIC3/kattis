r, c = map(int, input().split())
grid = [input() for _ in range(r)]
ans = [0] * 5
for i in range(r - 1):
    for j in range(c - 1):
        spaces = [grid[i + k][j + l] for k in range(2) for l in range(2)]
        if '#' not in spaces:
            ans[spaces.count('X')] += 1
print(*ans, sep='\n')
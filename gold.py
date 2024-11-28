import sys
sys.setrecursionlimit(2500)

def find(i, j):
    if grid[i][j] == '#': return 0
    gold = grid[i][j] == 'G'
    grid[i][j] = '#'
    if (grid[i - 1][j] == 'T' or
        grid[i + 1][j] == 'T' or
        grid[i][j - 1] == 'T' or
        grid[i][j + 1] == 'T'):
        return +gold
    gold += find(i - 1, j) + find(i + 1, j) + find(i, j - 1) + find(i, j + 1)
    return gold

w, h = map(int, input().split())
grid = [[*input()] for _ in range(h)]
print(next(find(i, j) for i in range(h) for j in range(w) if grid[i][j] == 'P'))
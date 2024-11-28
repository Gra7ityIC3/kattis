delta = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

def solve():
    r = c = ans = 0
    while 0 <= r < R and 0 <= c < C:
        if grid[r][c] == 'T': return ans
        if grid[r][c] == '#': return 'Lost'
        dr, dc = delta[grid[r][c]]
        grid[r][c] = '#'
        r += dr
        c += dc
        ans += 1
    return 'Out'

R, C = map(int, input().split())
grid = [[*input()] for _ in range(R)]
print(solve())
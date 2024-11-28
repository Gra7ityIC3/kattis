n, m = map(int, input().split())
g = [[*map(int, input().split())] for _ in range(n)]
print(min(sum(g[x][y] * (abs(i - x) + abs(j - y)) for x in range(n) for y in range(m)) for i in range(n) for j in range(m)))
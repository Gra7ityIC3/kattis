INF = 10 ** 9

n = int(input())
circles = [[*map(int, input().split())] for _ in range(n)]
AM = [[0] * n for _ in range(n)]
for i in range(n):
    x1, y1, r1 = circles[i]
    for j in range(i + 1, n):
        x2, y2, r2 = circles[j]
        AM[i][j] = AM[j][i] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 - r1 - r2
cost = [INF] * n
cost[0] = 0
taken = [False] * n
for _ in range(n - 1):
    _, u = min((cost[u], u) for u in range(n) if not taken[u])
    taken[u] = True
    for v in range(n):
        if not taken[v] and AM[u][v] < cost[v]:
            cost[v] = AM[u][v]
print(sum(cost))
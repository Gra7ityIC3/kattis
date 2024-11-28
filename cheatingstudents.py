INF = 10 ** 9

n = int(input())
points = [[*map(int, input().split())] for _ in range(n)]
AM = [[0] * n for _ in range(n)]
for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        AM[i][j] = AM[j][i] = abs(x1 - x2) + abs(y1 - y2)
cost = [INF] * n
cost[0] = 0
taken = [False] * n
for _ in range(n - 1):
    _, u = min((cost[u], u) for u in range(n) if not taken[u])
    taken[u] = True
    for v in range(n):
        if not taken[v] and AM[u][v] < cost[v]:
            cost[v] = AM[u][v]
print(sum(cost) * 2)
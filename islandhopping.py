import math

INF = 10 ** 9

for _ in range(int(input())):
    m = int(input())
    points = [[*map(float, input().split())] for _ in range(m)]
    AM = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            AM[i][j] = AM[j][i] = math.dist(points[i], points[j])
    cost = [INF] * m
    cost[0] = 0
    taken = [False] * m
    for _ in range(m - 1):
        _, u = min((cost[u], u) for u in range(m) if not taken[u])
        taken[u] = True
        for v in range(m):
            if not taken[v] and AM[u][v] < cost[v]:
                cost[v] = AM[u][v]
    print(sum(cost))
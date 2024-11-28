import math

INF = 10 ** 9

for _ in range(int(input())):
    input()
    n = int(input())
    points = [[*map(float, input().split())] for _ in range(n)]
    AM = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            AM[i][j] = AM[j][i] = math.dist(points[i], points[j])
    cost = [INF] * n
    cost[0] = 0
    taken = [False] * n
    for _ in range(n - 1):
        _, u = min((cost[u], u) for u in range(n) if not taken[u])
        taken[u] = True
        for v in range(n):
            if not taken[v] and AM[u][v] < cost[v]:
                cost[v] = AM[u][v]
    print(f'{sum(cost):.2f}')
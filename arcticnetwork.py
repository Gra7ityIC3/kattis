import math

INF = 10 ** 9

for _ in range(int(input())):
    s, p = map(int, input().split())
    points = [[*map(int, input().split())] for _ in range(p)]
    AM = [[0] * p for _ in range(p)]
    for i in range(p):
        for j in range(i + 1, p):
            AM[i][j] = AM[j][i] = math.dist(points[i], points[j])
    cost = [INF] * p
    cost[0] = 0
    taken = [False] * p
    for _ in range(p - 1):
        _, u = min((cost[u], u) for u in range(p) if not taken[u])
        taken[u] = True
        for v in range(p):
            if not taken[v] and AM[u][v] < cost[v]:
                cost[v] = AM[u][v]
    print(f'{sorted(cost)[-s]:.2f}')
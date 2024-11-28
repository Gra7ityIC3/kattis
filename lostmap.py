INF = 10 ** 9

n = int(input())
AM = [[*map(int, input().split())] for _ in range(n)]
parent, cost, taken = [0] * n, [INF] * n, [False] * n
cost[0] = 0
for _ in range(n - 1):
    _, u = min((cost[u], u) for u in range(n) if not taken[u])
    taken[u] = True
    for v in range(n):
        if not taken[v] and AM[u][v] < cost[v]:
            cost[v] = AM[u][v]
            parent[v] = u
for i in range(1, n):
    print(parent[i] + 1, i + 1)
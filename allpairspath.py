INF = 10 ** 9

while True:
    n, m, q = map(int, input().split())
    if n == 0: break
    D = [[INF] * n for _ in range(n)]
    for i in range(n): D[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        D[u][v] = min(D[u][v], w)
    for k in range(n):
        for i in range(n):
            if D[i][k] != INF:
                for j in range(n):
                    if D[k][j] != INF:
                        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    for k in range(n):
        for i in range(n):
            if D[i][k] != INF:
                for j in range(n):
                    if D[k][j] != INF and D[k][k] < 0:
                        D[i][j] = -INF
    for _ in range(q):
        u, v = map(int, input().split())
        print('Impossible' if D[u][v] == INF else '-Infinity' if D[u][v] == -INF else D[u][v])
    print()
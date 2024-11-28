from heapq import heappush, heappop

INF = 10 ** 18

n, m, t, d = map(int, input().split())
V = [1, *map(int, input().split()), n]
D = [[INF] * (n + 1) for _ in range((n + 1))]
for _ in range(m):
    i, j, k = map(int, input().split())
    D[i][j] = D[j][i] = k
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
AL = [[] for _ in range(n + 1)]
for u in V:
    for v in V:
        if u != v and D[u][v] <= d:
            AL[u].append((v, D[u][v]))
dist = [INF] * (n + 1)
dist[1] = 0
pq = [(0, 1)]
while pq:
    d, u = heappop(pq)
    if u == n:
        print(d)
        break
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
else:
    print('stuck')
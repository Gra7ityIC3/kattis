from heapq import heappush, heappop

INF = 10 ** 9

n, x, k = map(int, input().split())
h = [*map(int, input().split())]
AM = [[*map(int, input().split())] for _ in range(n)]
dist = [[INF] * (k + 1) for _ in range(n)]
dist[0][k] = 0
pq = [(0, 0, k)]
while pq:
    d, u, k = heappop(pq)
    if u == x - 1:
        print(d)
        break
    if d == dist[u][k]:
        for v in range(n):
            f = max(h[v] - h[u], 0)
            if k >= f and d + AM[u][v] < dist[v][k - f]:
                dist[v][k - f] = d + AM[u][v]
                heappush(pq, (dist[v][k - f], v, k - f))
else:
    print(-1)
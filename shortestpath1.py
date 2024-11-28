from heapq import heappush, heappop

INF = 10 ** 9

while True:
    n, m, q, s = map(int, input().split())
    if n == 0: break
    AL = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v, w))
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heappop(pq)
        if d == dist[u]:
            for v, w in AL[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))
    for _ in range(q):
        v = int(input())
        print('Impossible' if dist[v] == INF else dist[v])
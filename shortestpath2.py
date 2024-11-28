from heapq import heappush, heappop

INF = 10 ** 9

while True:
    n, m, q, s = map(int, input().split())
    if n == 0: break
    AL = [[] for _ in range(n)]
    for _ in range(m):
        u, v, t0, p, d = map(int, input().split())
        AL[u].append((v, t0, p, d))
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        t, u = heappop(pq)
        if t == dist[u]:
            for v, t0, p, d in AL[u]:
                c = t0 if t <= t0 else t0 + (t - t0 + p - 1) // p * p if p else INF
                if c + d < dist[v]:
                    dist[v] = c + d
                    heappush(pq, (dist[v], v))
    for _ in range(q):
        v = int(input())
        print('Impossible' if dist[v] == INF else dist[v])
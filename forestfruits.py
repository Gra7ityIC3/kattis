from heapq import heappush, heappop

INF = 10 ** 12

V, E, C, K, M = map(int, input().split())
AL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
    AL[v].append((u, w))
dist = [INF] * (V + 1)
dist[1] = 0
pq = [(0, 1)]
while pq:
    d, u = heappop(pq)
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
ans = [dist[f] for f in map(int, input().split()) if dist[f] != INF]
print(-1 if len(ans) < min(M, K) else 2 * sorted(ans)[min(M, K) - 1])
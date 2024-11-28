from heapq import heappush, heappop

INF = 10 ** 18

def dijkstra(k):
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heappop(pq)
        if u == n: return d
        if d == dist[u]:
            for v, w in AL[u]:
                if w <= k and d + w < dist[v]:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))
    return INF

n, m, x = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    c1, c2, t = map(int, input().split())
    AL[c1].append((c2, t))
    AL[c2].append((c1, t))
d = dijkstra(INF) * (100 + x) // 100
lo, hi = 0, 10 ** 9
while lo < hi:
    mid = (lo + hi) // 2
    if dijkstra(mid) <= d:
        hi = mid
    else:
        lo = mid + 1
print(hi)
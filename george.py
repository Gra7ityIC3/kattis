from heapq import heappush, heappop

INF = 10 ** 9

n, m = map(int, input().split())
a, b, k, g = map(int, input().split())
p = [*map(int, input().split())]
AL = [{} for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    AL[u][v] = AL[v][u] = (w, 0, 0)
t = -k
for u, v in zip(p, p[1:]):
    w = AL[u][v][0]
    AL[u][v] = AL[v][u] = (w, t, t + w)
    t += w
dist = [INF] * (n + 1)
dist[a] = 0
pq = [(0, a)]
while True:
    d, u = heappop(pq)
    if u == b:
        print(d)
        break
    if d == dist[u]:
        for v, (w, s, e) in AL[u].items():
            t = e if s <= d < e else d
            if t + w < dist[v]:
                dist[v] = t + w
                heappush(pq, (dist[v], v))
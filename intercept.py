from heapq import heappush, heappop

INF = 10 ** 18

n, m = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
s, t = map(int, input().split())
dist = [INF] * n
dist[s] = 0
pq = [(0, s)]
p = [[] for _ in range(n)]
while True:
    d, u = heappop(pq)
    if u == t: break
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                p[v] = [(u, w)]
                heappush(pq, (dist[v], v))
            elif d + w == dist[v]:
                p[v].append((u, w))
dist = [INF] * n
dist[t] = 0
pq = [(0, t)]
ans = []
while pq:
    d, u = heappop(pq)
    if not pq: ans.append(u)
    if d == dist[u]:
        for v, w in p[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
print(*sorted(ans))
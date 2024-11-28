from heapq import heappush, heappop

INF = 10 ** 9

V, E = map(int, input().split())
AL = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
s, t = map(int, input().split())
dist = [INF] * V
dist[s] = 0
ans = [0] * V
ans[s] = 1
pq = [(0, s)]
while pq:
    d, u = heappop(pq)
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                ans[v] = ans[u]
                heappush(pq, (dist[v], v))
            elif d + w == dist[v]:
                ans[v] += ans[u]
print(ans[t])
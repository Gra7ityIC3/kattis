from heapq import heappush, heappop

INF = 10 ** 9

n, m, x, y = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w, c = map(int, input().split())
    AL[a].append((b, w, c))
    AL[b].append((a, w, c))
dist = [(INF, INF, INF)] * (n + 1)
dist[x] = (0, 0, 0)
pq = [(0, 0, 0, x)]
while pq:
    t, s, d, u = heappop(pq)
    if u == y:
        print(d, s, t)
        break
    if (t, s, d) == dist[u]:
        for v, w, c in AL[u]:
            if (t + c // 2, s + c % 2, d + w) < dist[v]:
                dist[v] = (t + c // 2, s + c % 2, d + w)
                heappush(pq, (*dist[v], v))
else:
    print('IMPOSSIBLE')
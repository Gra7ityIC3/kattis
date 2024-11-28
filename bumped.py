from heapq import heappush, heappop

INF = 10 ** 12

n, m, f, s, t = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    i, j, c = map(int, input().split())
    AL[i].append((j, c))
    AL[j].append((i, c))
for _ in range(f):
    u, v = map(int, input().split())
    AL[u].append((v, 0))
dist = [[INF, INF] for _ in range(n)]
dist[s][1] = 0
pq = [(0, s, 1)]
while True:
    d, u, k = heappop(pq)
    if u == t:
        print(d)
        break
    if d == dist[u][k]:
        for v, w in AL[u]:
            if w and d + w < dist[v][k]:
                dist[v][k] = d + w
                heappush(pq, (dist[v][k], v, k))
            elif w == 0 and k and d < dist[v][k - 1]:
                dist[v][k - 1] = d
                heappush(pq, (dist[v][k - 1], v, k - 1))
from collections import deque

INF = 10 ** 9

n, m = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    AL[a].append((b, c))
    AL[b].append((a, c))
dist = [INF] * (n + 1)
dist[1] = 0
q = deque([(0, 1)])
while True:
    d, u = q.popleft()
    if u == n:
        print(d)
        break
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                q.append((dist[v], v)) if w else q.appendleft((dist[v], v))
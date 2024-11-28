from collections import deque

INF = 10 ** 9

n, h, l = map(int, input().split())
dist = [INF] * n
q = deque()
for x in map(int, input().split()):
    dist[x] = 0
    q.append(x)
AL = [[] for _ in range(n)]
for _ in range(l):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)
while q:
    u = q.popleft()
    for v in AL[u]:
        if dist[v] == INF:
            dist[v] = dist[u] + 1
            q.append(v)
print(dist.index(max(dist)))
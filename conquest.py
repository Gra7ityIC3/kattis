from heapq import *

n, m = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    AL[u].append(v)
    AL[v].append(u)
s = [0, *(int(input()) for _ in range(n))]
visited = [False] * (n + 1)
visited[1] = True
pq = []
for v in AL[1]:
    visited[v] = True
    pq.append((s[v], v))
heapify(pq)
while pq:
    d, u = heappop(pq)
    if d >= s[1]: break
    s[1] += d
    for v in AL[u]:
        if not visited[v]:
            visited[v] = True
            heappush(pq, (s[v], v))
print(s[1])
import sys
from heapq import heappush, heappop

sys.setrecursionlimit(1000000)

INF = 10 ** 9

def dfs(u):
    p.append(u)
    visited[u] = True
    if u == 1: return True
    for v, w in AL[u]:
        if not visited[v] and dist[u] != dist[v] + w and dfs(v):
            return True
    del p[-1]
    return False

n, m = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    AL[a].append((b, w))
    AL[b].append((a, w))
dist = [INF] * n
dist[1] = 0
pq = [(0, 1)]
while pq:
    d, u = heappop(pq)
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))

visited, p = [False] * n, []
if dfs(0):
    print(len(p), *p)
else:
    print('impossible')
from heapq import *

INF = 10 ** 9

n, k = map(int, input().split())
AL = [[] for _ in range(k + 1)]
dist = [[INF] * n for _ in range(n)]
pq = []
for r in range(n):
    for c, x in enumerate(map(int, input().split())):
        AL[x].append((r, c))
        if x == k:
            dist[r][c] = 0
            pq.append((0, r, c, k))
heapify(pq)
while pq:
    d, r, c, k = heappop(pq)
    if k == 1:
        print(d)
        break
    if d == dist[r][c]:
        for nr, nc in AL[k - 1]:
            w = abs(r - nr) + abs(c - nc)
            if d + w < dist[nr][nc]:
                dist[nr][nc] = d + w
                heappush(pq, (dist[nr][nc], nr, nc, k - 1))
else:
    print(-1)
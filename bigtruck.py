from heapq import heappush, heappop

INF = 10 ** 9

n = int(input())
t = [0, *map(int, input().split())]
AL = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b, d = map(int, input().split())
    AL[a].append((b, d))
    AL[b].append((a, d))
dist = [INF] * (n + 1)
dist[1] = 0
ans = [0] * (n + 1)
ans[1] = t[1]
pq = [(0, 1)]
while pq:
    d, u = heappop(pq)
    if d == dist[u]:
        for v, w in AL[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                ans[v] = ans[u] + t[v]
                heappush(pq, (dist[v], v))
            elif d + w == dist[v] and ans[u] + t[v] > ans[v]:
                ans[v] = ans[u] + t[v]
if dist[n] == INF:
    print('impossible')
else:
    print(dist[n], ans[n])
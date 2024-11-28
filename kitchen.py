from heapq import heappush, heappop

INF = 10 ** 9

n, *c, V = map(int, input().split())
dist = {(c[0], 0, 0, 0, 0): 0}
pq = [(0, (c[0], 0, 0, 0, 0))]
while pq:
    d, u = heappop(pq)
    if u[0] == V:
        print(d)
        break
    if d == dist[u]:
        for i in range(n):
            if u[i] == 0: continue
            for j in range(n):
                if i == j or u[j] == c[j]: continue
                w = min(u[i], c[j] - u[j])
                v = [*u]; v[i] -= w; v[j] += w; v = (*v,)
                if d + w < dist.get(v, INF):
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))
else:
    print('impossible')
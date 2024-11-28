from heapq import heappush, heappop

INF = 10 ** 9

N, S, T = map(int, input().split())
D = [[*map(int, input().split())] for _ in range(N)]
dist = [INF] * N
dist[S] = 0
pq = [(0, S)]
while True:
    d, u = heappop(pq)
    if u == T:
        print(d)
        break
    if d == dist[u]:
        for v in range(N):
            if d + D[u][v] < dist[v]:
                dist[v] = d + D[u][v]
                heappush(pq, (dist[v], v))
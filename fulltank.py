from heapq import heappush, heappop

INF = 10 ** 9

n, m = map(int, input().split())
p = [*map(int, input().split())]
AL = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, input().split())
    AL[u].append((v, d))
    AL[v].append((u, d))
for _  in range(int(input())):
    c, s, e = map(int, input().split())
    dist = [[INF] * (c + 1) for _ in range(n)]
    dist[s][0] = 0
    pq = [(0, s, 0)]
    while pq:
        t, u, f = heappop(pq)
        if u == e:
            print(t)
            break
        if t == dist[u][f]:
            if f < c and t + p[u] < dist[u][f + 1]:
                dist[u][f + 1] = t + p[u]
                heappush(pq, (t + p[u], u, f + 1))
            for v, d in AL[u]:
                if f >= d and t < dist[v][f - d]:
                    dist[v][f - d] = t
                    heappush(pq, (t, v, f - d))
    else:
        print('impossible')
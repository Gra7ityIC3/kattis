from heapq import heappush, heappop

INF = 10 ** 12

n, m, p = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    u, v, w, c = input().split()
    u, v, w = int(u), int(v), int(w)
    AL[u].append((v, w, c))
    AL[v].append((u, w, c))
for _ in range(p):
    a, b = map(int, input().split())
    dist = [(INF, INF)] * n
    dist[a] = (0, 0)
    pq = [(0, 0, a)]
    while pq:
        t, d, u = heappop(pq)
        if u == b:
            print(t, d)
            break
        if (t, d) == dist[u]:
            for v, w, c in AL[u]:
                if (t + w * (c == 'O'), d + w) < dist[v]:
                    dist[v] = (t + w * (c == 'O'), d + w)
                    heappush(pq, (*dist[v], v))
    else:
        print('IMPOSSIBLE')
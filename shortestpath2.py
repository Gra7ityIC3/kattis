from heapq import heappush, heappop

INF = 10 ** 9

while True:
    n, m, q, s = map(int, input().split())

    if n == 0:
        break

    AL = [[] for _ in range(n)]

    for _ in range(m):
        u, v, t0, P, d = map(int, input().split())
        AL[u].append((v, t0, P, d))

    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        time, u = heappop(pq)

        if time != dist[u]:
            continue

        for v, t0, P, d in AL[u]:
            if time <= t0:
                new_time = t0
            elif P == 0:
                continue
            else:
                t = (time - t0 + P - 1) // P
                new_time = t0 + t * P

            if new_time + d < dist[v]:
                dist[v] = new_time + d
                heappush(pq, (dist[v], v))

    for _ in range(q):
        v = int(input())
        print('Impossible' if dist[v] == INF else dist[v])
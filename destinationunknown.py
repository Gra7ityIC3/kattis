from heapq import heappush, heappop

INF = 10 ** 9

for _ in range(int(input())):
    n, m, t = map(int ,input().split())
    s, g, h = map(int, input().split())
    AL = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int ,input().split())
        AL[a].append((b, d))
        AL[b].append((a, d))
    dist = [[INF, INF] for _ in range(n + 1)]
    dist[s][0] = 0
    pq = [(0, s, 0)]
    while pq:
        d, u, gh = heappop(pq)
        if d == dist[u][gh]:
            for v, w in AL[u]:
                gh_used = gh or (u, v) == (g, h) or (u, v) == (h, g)
                if d + w < dist[v][gh_used]:
                    dist[v][gh_used] = d + w
                    heappush(pq, (dist[v][gh_used], v, gh_used))
    ans = []
    for _ in range(t):
        x = int(input())
        if dist[x][0] >= dist[x][1] != INF:
            ans.append(x)
    print(*sorted(ans))
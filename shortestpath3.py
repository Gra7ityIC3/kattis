INF = 10 ** 9

def dfs(u):
    visited[u] = True
    for v, w in AL[u]:
        if not visited[v]:
            dfs(v)

while True:
    n, m, q, s = map(int, input().split())
    if n == 0: break
    AL = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v, w))
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n
    for i in range(n):
        for u in range(n):
            if dist[u] != INF:
                for v, w in AL[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        if i == n - 1: dfs(v)
    for _ in range(q):
        v = int(input())
        print('Impossible' if dist[v] == INF else '-Infinity' if visited[v] else dist[v])
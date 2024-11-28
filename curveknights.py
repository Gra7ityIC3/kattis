def dfs(u):
    visited[u] = True
    for v, w in AL[u]:
        if not visited[v]:
            dfs(v)
        a[u] += a[v] * w

n, m = map(int, input().split())
a = [*map(int, input().split())]
AL = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    AL[u].append((v, w))
visited = [False] * n
for u in range(n):
    if not visited[u]:
        dfs(u)
print(*a)
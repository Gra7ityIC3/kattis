def dfs(u):
    visited[u] = True
    for v in AL[u]:
        if not visited[v]:
            dfs(v)

for _ in range(int(input())):
    n = int(input())
    AL = [[] for _ in range(n)]
    for _ in range(int(input())):
        u, v = map(int, input().split())
        AL[u].append(v)
        AL[v].append(u)
    visited, ans = [False] * n, -1
    for u in range(n):
        if not visited[u]:
            ans += 1
            dfs(u)
    print(ans)
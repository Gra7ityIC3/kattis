def dfs(u):
    visited[u] = True
    for v in range(n):
        if not visited[v] and AM[u][v] == '1':
            dfs(v)
    ans.append(u)

n = int(input())
AM = [input() for _ in range(n)]
visited, ans = [False] * n, []
dfs(0)
if len(ans) == n:
    print(*ans)
else:
    print('impossible')
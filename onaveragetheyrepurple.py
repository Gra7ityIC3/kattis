from collections import deque

n, m = map(int, input().split())
AL = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)
dist = [-1] * (n + 1)
q = deque([1])
while dist[n] == -1:
    u = q.popleft()
    for v in AL[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
print(dist[n])
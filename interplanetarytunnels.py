from collections import deque

n, m = map(int, input().split())
pa, pb = map(int, input().split())
AL = [[] for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    AL[p1].append(p2)
    AL[p2].append(p1)
dist = [-1] * n
dist[pa] = 0
q = deque([pa])
while True:
    u = q.popleft()
    if u == pb:
        print((dist[pb] + 1) // 2)
        break
    for v in AL[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
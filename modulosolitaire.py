from collections import deque

m, n, s0 = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
dist = [-1] * m
dist[s0] = 0
q = deque([s0])
while q and dist[0] == -1:
    u = q.popleft()
    for i in range(n):
        v = (u * a[i] + b[i]) % m
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)
print(dist[0])
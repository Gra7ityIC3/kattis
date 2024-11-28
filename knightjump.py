from collections import deque

dr = (2, 2, -2, -2, 1, 1, -1, -1)
dc = (1, -1, 1, -1, 2, -2, 2, -2)

n = int(input())
dist = [[-1] * n for _ in range(n)]
q = deque()
for i in range(n):
    for j, c in enumerate(input()):
        if c == '#':
            dist[i][j] = 0
        elif c == 'K':
            dist[i][j] = 0
            q.append((i, j))
while q and dist[0][0] == -1:
    r, c = q.popleft()
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
print(dist[0][0])